import numpy as np
import matplotlib

arr = np.empty((0, 2))

inputFile = open("CdSe_CdZnS Core_Shell.txt", "r")
arr = np.array([list(map(float, line.strip().replace(",", ".").split("\t"))) for line in inputFile])
outputFile = open("output.txt", "w")

outputFile.write(f"{np.mean(arr, 0)} {np.std(arr, 0)}")