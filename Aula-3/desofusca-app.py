import sys
from eVotUM.Cripto import eccblind


def printUsage():
    print("Usage: python desofusca-app.py -s <Blind Signature> -RDash <pRDashComponents>")

def parseArgs():
    if (len(sys.argv) < 5):
        printUsage()
    else:
        if(sys.argv[1]=="-s" and sys.argv[3]=="-RDash"):
            main()
        else:
            printUsage()

def showResults(errorCode, signature):
    print("Output")
    if (errorCode is None):
        print("Signature: %s" % signature)
    elif (errorCode == 1):
        print("Error: pRDash components are invalid")
    elif (errorCode == 2):
        print("Error: blind components are invalid")
    elif (errorCode == 3):
        print("Error: invalid blind signature format")

def main():
    print("Input")
    file = open("requerente.txt", "r")
    blindSignature = sys.argv[2]
    blindComponents = file.readline()[:-1]
    pRDashComponents = sys.argv[4]
    errorCode, signature = eccblind.unblindSignature(blindSignature, pRDashComponents, blindComponents)
    showResults(errorCode, signature)

if __name__ == "__main__":
    parseArgs()
