# COMPSS-211 Final Project: What Is An American?

Template repository for the MaCSS Advanced Computing final project.

## Contributors
- Willow McLarney  
- Shreya Annamaneni  
- Rachel Avram  

---

## Project Overview

This repo contains our full workflow for analyzing how U.S. presidents talk about “Americans” and “others” over time.

We look at American in-group and out-group sentiment and identity in three main ways:

1. **Group sentiment:** sentiment scores attached to different demographic groups.  
2. **Identity content:** which traits and adjectives are treated as more or less “American.”  
3. **Temporal patterns:** how “us vs them” language and identity themes shift across U.S. history.

All analysis is done on presidential speeches from a [kaggle dataset](ADD LINK), which was pulled from the [American Presidency Project](https://www.presidency.ucsb.edu/)

---

## Repo Structure

```text
data/
    all_speeches.csv
    _20_percent_sample.csv
    demographic_group_american_nonamerican_similarity_results.csv
    in_group_words_key.csv
    out_group_words_key.csv
    sample_speeches_llm_enriched.csv
    speeches_w_demographic_categories_llm_enriched.csv
    vader_validation_sample.csv

notebooks/
    Temporal.ipynb
    Vader_Group_Sentiment.ipynb
    llm_adj_analysis.ipynb
    preliminary_eda.ipynb

scripts/
    create_dataframe.py


````markdown
# COMPSS-211 Final Project: What Is An American?

Template repository for the MaCSS Advanced Computing final project.

## Contributors
- Willow McLarney  
- Shreya Annamaneni  
- Rachel Avram  

---

## Project Overview

This repo contains our full workflow for analyzing how U.S. presidents talk about “Americans” and “others” over time.

We look at American in-group and out-group sentiment and identity in three main ways:

1. **Group sentiment:** sentiment scores attached to different demographic groups.  
2. **Identity content:** which traits and adjectives are treated as more or less “American.”  
3. **Temporal patterns:** how “us vs them” language and identity themes shift across U.S. history.

All analysis is done on presidential speeches, and all use of LLMs is documented in the notebooks.

---

## Repo Structure

```text
data/
    all_speeches.csv
    _20_percent_sample.csv
    demographic_group_american_nonamerican_similarity_results.csv
    in_group_words_key.csv
    out_group_words_key.csv
    sample_speeches_llm_enriched.csv
    speeches_w_demographic_categories_llm_enriched.csv
    vader_validation_sample.csv

notebooks/
    Temporal.ipynb
    Vader_Group_Sentiment.ipynb
    llm_adj_analysis.ipynb
    preliminary_eda.ipynb

scripts/
    create_dataframe.py
````

---

## Data Files

All main data files live in `data/`. Here is how each one is used.

* **`all_speeches.csv`**
  Main dataframe of presidential speeches. Contains one row per speech, with metadata (date, year, president, title) and transcript text.
  Used in:

  * regex “us vs them” counts
  * VADER sentence sentiment over time
  * some demographic matching

Created with: create_dataframe.py script 

* **`demographic_group_american_nonamerican_similarity_results.csv`**
  Output from the embedding analysis using all-MiniLM. Contains similarity scores between each demographic group and in-group vs out-group adjective vectors, plus the “net difference” metric.
  Used in:

  * group-level “how American vs non-American” similarity results

* **`in_group_words_key.csv`**
  Mapping of in-group adjectives to higher-level identity themes. Each row has a theme name and a list of adjectives that fall under that theme.

* **`out_group_words_key.csv`**
  Mapping of out-group adjectives to themes. Same format as the in-group file.

* **`sample_speeches_llm_enriched.csv`**
  LLM-enriched 20% sample of speeches. Contains:

  * lists of in-group adjectives
  * lists of out-group adjectives
  * demographic group mentions (from LLM prompts)
    This is the “raw” LLM output 
    
* **`_20_percent_sample.csv`**
  Clean 20% random sample of speeches derived from `sample_speeches_llm_enriched.csv` with a simplified set of columns.
  Used in:

  * temporal analysis of LLM adjective themes (decade plots, stable vs changing themes)

* **`speeches_w_demographic_categories_llm_enriched.csv`**
  Version of the speech data with LLM-coded demographic categories attached.
  Used in:

  * group sentiment with VADER
  * embedding analysis by race, religion, nationality, immigration status, and ideology

* **`vader_validation_sample.csv`**
  Hand-audited sample of “us_only” and “them_only” sentences with their VADER scores for temporal analysis.
  Used in:
  
  * validating how well VADER handles older and more formal presidential language

---

## Notebooks

All analysis code lives in `notebooks/`. They can be run independently if the data files above are present.

* **`preliminary_eda.ipynb`**
  Early exploration of the speech corpus and types, basic checks on dates, presidents, and text fields.

* **`Vader_Group_Sentiment.ipynb`**
  Group-level sentiment analysis:

  * uses SpaCy NER to find NORP groups
  * runs VADER on sentences that mention those groups
  * summarizes sentiment attached to different demographic labels

* **`llm_adj_analysis.ipynb`**
  LLM adjective and embedding work:

  * cleans LLM output for in-group and out-group adjectives
  * builds the adjective theme dictionaries
  * calculates cosine similarity between adjectives and demographic group embeddings
  * produces the “how American vs non-American” similarity results

* **`Temporal.ipynb`**
  Temporal analysis notebook:

  * regex counts of “us” vs “them/othering” over time
  * VADER sentiment for “us” vs “them/other” sentences over time
  * decade-level trends in LLM adjective themes and stable vs changing identity themes

---

## Scripts

* **`scripts/create_dataframe.py`**
  Script for building `all_speeches.csv` from the raw speech files.

  Basic usage from the repo root:

  ```bash
  python scripts/create_dataframe.py
  ```

  The script reads the raw speech data, cleans and combines them, and writes the final CSV to `data/all_speeches.csv`.
  If you only want to reproduce the analysis and not regenerate the corpus, you can skip this step because `all_speeches.csv` is already included.

---

## How to Run the Project

1. **Clone the repo and set up an environment**

   ```bash
   git clone <this-repo-url>
   cd COMPSS-211-Final-Project-Template-Repo
   ```

   Install Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   *(If you do not have a `requirements.txt`, you will need packages like `pandas`, `numpy`, `matplotlib`, `scikit-learn`, `spacy`, `vaderSentiment`, and `sentence-transformers`.)*

2. **Create `all_speeches.csv`**
   If you want to rebuild the main dataframe from raw files:

   ```bash
   python scripts/create_dataframe.py
   ```

3. **Open the notebooks**

   Start Jupyter or VS Code and open notebooks in this rough order if you want to follow our workflow:

   1. `preliminary_eda.ipynb`
   2. `Vader_Group_Sentiment.ipynb`
   3. `llm_adj_analysis.ipynb`
   4. `Temporal.ipynb`

   Running these notebooks will reproduce the figures and tables from the final report. Some cells may write new CSVs into `data/` while saving intermediate results.


