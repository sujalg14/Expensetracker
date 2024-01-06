totalBalance = 0


class Transaction:
    type = None  # debit or credit
    amount = None  # amount of transaction
    description = None
    comments = None  # additional comments
    date = None  # date of transaction
    acc = None  # accont number
    bank = None  # bank
    tags = []  # tags related to transaction
    availableBalance = None  # available balance until this transaction

    def addTransaction(myself, type, description, comments, amount, acc, bank, tags, date=None):
        global totalBalance
        myself.type = type
        myself.description = description
        myself.amount = amount
        myself.comments = comments
        myself.acc = acc
        myself.bank = bank
        myself.tags = tags.split(",")
        if date is not None:
            myself.date = date
        else:
            myself.date = date.today().strftime("%d/%m/%Y")
        if type == "Debit":
            myself.availableBalance = totalBalance - amount
            totalBalance = myself.availableBalance

        else:
            myself.availableBalance = totalBalance + (amount)
            totalBalance = myself.availableBalance

    def printTransaction(self):
        print(">>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print("Type: " + self.type)
        print("description: " + self.description)
        print("amount: " + str(self.amount))
        print("availableBalance: " + str(self.availableBalance))
        print("comments: " + self.comments)
        print("tags: " + str(self.tags))
        print("date: " + self.date)
        print("acc: " + self.acc)
        print("bank: " + self.bank)
        print(">>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n\n")
