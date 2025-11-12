import requests
import pandas as pd
from collections import Counter
from datetime import datetime
import matplotlib.pyplot as plt
import sys

# Lettura argomenti da riga di comando
if len(sys.argv) != 3:
    print("Uso: python github-repo-issue-monthly.py <owner> <repo>")
    sys.exit(1)

owner = sys.argv[1]
repo = sys.argv[2]

# API GitHub
url = f"https://api.github.com/repos/{owner}/{repo}/issues"
params = {
    "state": "all",
    "per_page": 100,
    "page": 1
}
headers = {
    "Accept": "application/vnd.github.v3+json"
}

# Raccolta issue
print(f"Raccogliendo issue da {owner}/{repo}...")
issues = []
while True:
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    if not data or "message" in data:
        break
    issues.extend([i for i in data if "pull_request" not in i])  # esclude PR
    params["page"] += 1
    print(f"Pagina {params['page'] - 1} completata...")

print(f"Totale issue trovate: {len(issues)}")

# Estrazione date
created_months = [
    datetime.strptime(issue["created_at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m")
    for issue in issues
]

# Conteggio per mese
monthly_counts = Counter(created_months)
df = pd.DataFrame(sorted(monthly_counts.items()), columns=["Mese", "Numero Issue"])

# Grafico
plt.figure(figsize=(12, 6))
plt.bar(df["Mese"], df["Numero Issue"], color="skyblue")
plt.xticks(rotation=45)
plt.title(f"Issue aperte per mese - {owner}/{repo}")
plt.xlabel("Mese")
plt.ylabel("Numero di issue")
plt.tight_layout()

# Salva il grafico invece di mostrarlo
output_file = f"{owner}_{repo}_issues.png"
plt.savefig(output_file, dpi=300, bbox_inches='tight')
print(f"\nGrafico salvato come: {output_file}")

# Salva anche i dati in CSV
csv_file = f"{owner}_{repo}_issues.csv"
df.to_csv(csv_file, index=False)
print(f"Dati salvati come: {csv_file}")