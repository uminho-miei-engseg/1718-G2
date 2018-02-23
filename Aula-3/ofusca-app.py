import sys
from eVotUM.Cripto import eccblind


def printUsage():
    print("Usage: python ofusca-app.py -msg <mensagem a assinar> -RDash <pRDashComponents>")

def parseArgs():
    if (len(sys.argv) < 5):
        printUsage()
    else:
        if(sys.argv[1]=="-msg" and sys.argv[3]=="-RDash"):
            main()
        else:
            printUsage()

def showResults(errorCode, result):
    print("Output")
    if (errorCode is None):
        blindComponents, pRComponents, blindM = result
        print("Blind message: %s" % blindM)
        file = open("requerente.txt", "w")
        file.write(blindComponents)
        file.write("\n")
        file.write(pRComponents)
        file.write("\n")
    elif (errorCode == 1):
        print("Error: pRDash components are invalid")

def main():
    print("Input")
    data = sys.argv[2]
    pRDashComponents = sys.argv[4]
    errorCode, result = eccblind.blindData(pRDashComponents, data)
    showResults(errorCode, result)

if __name__ == "__main__":
    parseArgs()
