import sys
from eVotUM.Cripto import eccblind

def printUsage():
    print("Usage: python init-app.py or python init-app.py -init")

def parseArgs():
    if (len(sys.argv) > 1):
        if(sys.argv[1]=="-init"):
            main()
        else:
            printUsage()
    else:
        imprimeR()

def imprimeR():
    initComponents, pRDashComponents = eccblind.initSigner()
    print (pRDashComponents);

def main():
    initComponents, pRDashComponents = eccblind.initSigner()
    file = open("assinante.txt", "w")
    file.write(initComponents)
    file.write("\n")
    file.write(pRDashComponents)
    file.write("\n")
    file.close()

if __name__ == "__main__":
    parseArgs()
