# Notícies en un minut

Cada matí, aquest projecte busca notícies als diaris en línia (Catalunya, Espanya i món), les tria perquè siguin interessants per a un nen de 13 anys i les reescriu en català fàcil, neutral i d'1 minut de lectura. Tot es publica sol en una pàgina web.

## Com funciona

1. `fetch_news.py` llegeix els feeds RSS de `feeds.json`.
2. Claude tria les notícies més adequades de cada tema.
3. Llegeix l'article original (i el d'altres diaris sobre el mateix fet, per contrastar).
4. Claude les reescriu amb paraules pròpies, amb glossari i una pregunta de comprensió.
5. Es desa `docs/news.json` i `docs/index.html` el mostra.
6. GitHub Actions ho repeteix cada dia (`.github/workflows/daily.yml`).

## Posada en marxa (una sola vegada)

1. **Crea un repositori a GitHub** i puja tot el contingut d'aquesta carpeta (inclosa la carpeta oculta `.github`).
2. **Clau de l'API:** crea-la a https://console.anthropic.com i, al repositori, ves a *Settings → Secrets and variables → Actions → New repository secret*. Nom: `ANTHROPIC_API_KEY`.
3. **Pàgina web:** *Settings → Pages → Build and deployment → Deploy from a branch → Branch: main, carpeta /docs → Save*.
4. **Primera execució:** pestanya *Actions → Notícies del dia → Run workflow*. Tarda uns minuts.
5. Obre l'adreça que et dona *Settings → Pages* (normalment `https://EL-TEU-USUARI.github.io/NOM-REPO/`). Pots afegir-la a la pantalla d'inici del mòbil.

A partir d'aquí s'actualitza sola cada matí.

## Comprovar els feeds (important)

Alguns diaris canvien les adreces dels seus RSS. Si pots, executa-ho a un ordinador:

    pip install -r requirements.txt
    python check_feeds.py

Els que surtin amb `ERROR` s'han de substituir a `feeds.json` per l'adreça RSS actual del diari. Si un feed falla, el programa continua amb la resta, i als registres d'Actions hi surt un avís.

## Personalitzar

- **Temes i diaris:** edita `feeds.json`.
- **Nombre de notícies per tema:** variable `STORIES_PER_CATEGORY` (per defecte 2).
- **Model:** variable `CLAUDE_MODEL`.
- **Hora:** línia `cron` de `daily.yml` (és en hora UTC).

## Cost i limitacions

- Unes 20 crides a l'API per dia: normalment uns pocs cèntims.
- Els resums els fa una IA i poden tenir errors; la pàgina sempre enllaça les fonts originals.
- Alguns diaris tenen mur de pagament: en aquest cas el resum es fa només amb el titular i l'entradeta, i es descarta la notícia si no hi ha prou informació.
- Si el repositori és públic, la pàgina també ho és. Per a ús familiar és recomanable no difondre-la àmpliament, ja que reprodueix resums de diaris.
