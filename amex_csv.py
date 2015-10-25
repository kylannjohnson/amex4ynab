#!/usr/bin/python
import fileinput

class Transaction(object):
    """docstring for Transaction"""
    def __init__(self, lineString):
        super(Transaction, self).__init__()
        items = self.makeItems(lineString)
        self.date = self.parseDate(items[0])
        self.payee = items[2]
        self.payer = items[3]
        self.card = items[4]
        self.amount = items[7]

    def makeItems(self, lineStr):
        return lineStr.split(',')

    def parseDate(self, dateStr):
        if dateStr.find("Mon") >= 0:
            self.date = dateStr.replace("  Mon", "")
        elif dateStr.find("Tue") >= 0:
            self.date = dateStr.replace("  Tue", "")
        elif dateStr.find("Wed") >= 0:
            self.date = dateStr.replace("  Wed", "")
        elif dateStr.find("Thu") >= 0:
            self.date = dateStr.replace("  Thu", "")
        elif dateStr.find("Fri") >= 0:
            self.date = dateStr.replace("  Fri", "")
        elif dateStr.find("Sat") >= 0:
            self.date = dateStr.replace("  Sat", "")
        elif dateStr.find("Sun") >= 0:
            self.date = dateStr.replace("  Sun", "")
        else:
            print "NOT FOUND"

        return self.date

    def printAsLine(self):
        print self.asString()

    def asString(self):
        return "%s,%s,%s,%s,%s" % (self.date, self.payee, self.payer, self.card, self.amount)


if __name__ == "__main__":

    def headers():
        return "%s,%s,%s,%s,%s" % ("Date", "Payee", "Payer", "Card", "Outflow")

    def toFile(name, transactions):
        splitName = name.split('.')

        outFileName = splitName[0] + ".formatted." + splitName[1]

        target = open(outFileName, 'w')

        target.write(headers() + "\n")
        for trans in transactions:
            target.write(trans.asString() + "\n")

        target.close()


    transactions = []

    for line in fileinput.input():
        transactions.append(Transaction(line))

    print headers()
    for trans in transactions:
        trans.printAsLine()

    toFile(fileinput.filename(), transactions)

    fileinput.close()
