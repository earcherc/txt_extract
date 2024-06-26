import os
import pandas as pd


def extract_texts_to_csv(folder_path, output_csv_file):
    # List to hold the data
    data = []

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):  # Check for text files
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()  # Read the content of the file
                data.append(
                    [filename, content]
                )  # Append the filename and content to the list

    # Create a DataFrame
    df = pd.DataFrame(data, columns=["Filename", "Content"])

    # Write DataFrame to CSV
    df.to_csv(output_csv_file, index=False)


# Usage example: update 'your_folder_path' and 'your_output_file.csv' with your specifics
extract_texts_to_csv("txt_files", "output.csv")
