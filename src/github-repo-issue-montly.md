# Numero issue GitHub di un repository aperte per mese

Semplice script che esegue il rendering di un grafico che 
mostra il numero di issue per mese per un repository GitHub.

Vengono considerate tutte le issue inserite in un dato mese, 
indipendentemente dello stato.

[indice](../README.md)

## Requirement

- Python 3.14.0+

```xml
pip install requests pandas matplotlib
```

## Utilizzo

```xml
python github-repo-issue-montly.py ${org} ${repo}
```

Ad esempio per il progetto : 

<https://github.com/fugerit-org/fj-doc>

```xml
python github-repo-issue-montly.py fugerit-org fj-doc
```

Ecco lo script [github-repo-issue-montly.py](github-repo-issue-montly.py)