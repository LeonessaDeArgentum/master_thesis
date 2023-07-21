from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--filein", dest="filein",
                  help="file with tabled TSS from base", metavar="FILE")
parser.add_option("-o", "--fileout", dest="fileout",
                  help="name of the output file", metavar="FILE")
(options, args) = parser.parse_args()


filein = open(options.filein, 'r')
fileout = open(options.fileout, 'w')
temp = filein.readline()
inlines = filein.readlines()
ntss = 1
for line in inlines:
    vectorline = line.split('\t')
    if vectorline[6] == "YES" and vectorline[7] != "NA":
        outline = "\t".join([vectorline[0], vectorline[7],vectorline[7],vectorline[3], "TSS"+str(ntss)])
        ntss += 1
        fileout.write(outline+"\n")

print("Script executed.")


