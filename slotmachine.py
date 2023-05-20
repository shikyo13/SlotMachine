import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbolcount = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbolvalues = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def getslotspin(rows, cols, symbols):
    allsymbols = []
    weights = []
    for symbol, symbolcount in symbols.items():
        allsymbols.append(symbol)
        weights.append(symbolcount)
            
    columns = []
    for _ in range(cols):
        column = random.choices(allsymbols, weights=weights, k=rows)
        columns.append(column)
    
    return columns

def printslots(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
                          
def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
            
    return amount

def getlines():
    while True:
        lines = input("How many lines would you like to bet on? 1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Number of lines must be between 1-" + str(MAX_LINES) + ")")
        else:
            print("Please enter a number.")
            
    return lines

def getbet():
    while True:
        bet = input("How much would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
            
    return bet

def checkwinnings(columns, lines, bet, values):
    winnings = 0
    winninglines =[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbolcheck = column[line]
            if symbol != symbolcheck:
                break
        else:
            winnings += values[symbol] * bet
            winninglines.append(line + 1)
    
    return winnings, winninglines

def spin(balance):
    lines = getlines()
    while True:
        bet = getbet()
        totalbet = bet * lines
        
        if totalbet > balance:
            print(f"You don't have enough to cover this bet, your current balance is ${balance}")
        else:
            break
            
    print(f"You are betting ${bet} on {lines}. Total bet is equal to: ${totalbet}")
    
    slots = getslotspin(ROWS, COLS, symbolcount)
    printslots(slots)
    winnings, winninglines = checkwinnings(slots, lines, bet, symbolvalues)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winninglines)
    return winnings - totalbet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play. (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")
        
main()