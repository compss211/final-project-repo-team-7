import os
from pathlib import Path
import pandas as pd

def build_df_from_json_files(json_folder, output_file):
    """
    Combines all JSON files in `json_folder` into one DataFrame.
    If `output_file` already exists, loads it instead of rebuilding.
    """
    # check if file already exists
    if os.path.exists(output_file):
        print(f"File already exists")
        return
    else:
        # if file doesn't exist, combine files within `json_folder` into a dataframe
        print("Building new combined DataFrame from JSON files")
        paths = Path(json_folder).glob("*.json")
        df = pd.DataFrame([pd.read_json(p, typ="series") for p in paths])
        print(f"Combined DataFrame saved to {output_file}")
        # save to path specified by `output_file` 
        df.to_csv(output_file)

    return 

# preparing for execution in terminal
if __name__ == "__main__":
    json_folder = "../data/speeches" # source of json files 
    output_file = "../data/all_speeches.csv" # path for combined dataframe

    df = build_df_from_json_files(json_folder, output_file)
