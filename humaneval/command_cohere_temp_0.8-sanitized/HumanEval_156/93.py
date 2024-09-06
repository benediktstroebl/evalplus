def int_to_mini_roman(n):
    if n < 1:
        return ""

    symbols = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"]
    tens = ["","x","l","c","d","m"]
    hundreds = ["","c","cc","ccc","cd","cm"]

    roman = []

    for digit in str(n):
        if digit == '1':
            roman.append(symbols[0])
        elif digit == '2':
            roman.append(symbols[1])
        elif digit == '3':
            roman.append(symbols[2])
        elif digit == '4':
            roman.append(symbols[3])
        elif digit == '5':
            roman.append(symbols[4])
        elif digit == '6':
            roman.append(symbols[5])
        elif digit == '7':
            roman.append(symbols[6])
        elif digit == '8':
            roman.append(symbols[7])
        elif digit == '9':
            roman.append(symbols[8])
        elif digit == '0':
            pass
        else:
            print(f"Error: {digit} not recognized.")
            return ""

    roman = [ten + hundred + rom for hundred in hundreds for ten in tens for rom in roman]
    return ''.join(roman).lower()