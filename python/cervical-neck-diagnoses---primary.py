# Romi Haas, Ljoudmila Busija, Alexandra Gorelik, Denise A O'Connor, Christopher Pierce, Danielle Mazza, Rochelle Buchbinder, 2024.

import sys, csv, re

codes = [{"code":"387801000.0","system":"snomedct"},{"code":"11049006.0","system":"snomedct"},{"code":"54404000.0","system":"snomedct"},{"code":"72535009.0","system":"snomedct"},{"code":"81099000.0","system":"snomedct"},{"code":"202664003.0","system":"snomedct"},{"code":"425878001.0","system":"snomedct"},{"code":"445429009.0","system":"snomedct"},{"code":"95671001.0","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('neck-diagnoses-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cervical-neck-diagnoses---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cervical-neck-diagnoses---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cervical-neck-diagnoses---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
