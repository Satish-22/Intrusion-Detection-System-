import csv

def txt_to_csv(input_file, output_file):
    with open(input_file, 'r') as txt_file:
        # Read the lines from the .txt file and split by tabs
        lines = [line.strip().split('\t') for line in txt_file]

    with open(output_file, 'w', newline='') as csv_file:
        # Use csv.writer to write the data to the .csv file without any quotation marks
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_NONE)
        csv_writer.writerows(lines)

if __name__ == "__main__":
    # Replace 'input.txt' and 'output.csv' with your file names
    txt_file_path = 'KDDTrain+.txt'
    csv_file_path = 'KDDTrain_label.csv'

    txt_to_csv(txt_file_path, csv_file_path)
    print("Conversion complete. File saved as output.csv.")
