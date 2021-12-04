#!/usr/bin/python

import argparse,sys,getopt,csv

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s 1.0', help="Show program's version number and exit.")

parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='process_query.py --input <input_filename_name> --output <output_file_name>')

parser.add_argument('-o', '--output', required=True,help="output file")

parser.add_argument('-i','--input', required=True,help='Input file')

args = parser.parse_args()

if args.output:
    print("Processing the data")
    with open(args.input) as csv_file , open(args.output,"w") as output:
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	    for row in csv_reader:
	        writer.writerow([row[0],row[1],row[18]])
