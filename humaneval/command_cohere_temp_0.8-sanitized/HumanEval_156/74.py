def int_to_mini_roman(n):
    if n < 1:
        return ""

    symbols = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"]
    tens = ["","x","l","c","d","m"]
    hundreds = ["","c","cc","ccc","cd","cm"]

    roman = []
    for i in range(0, len(symbols) - 1):
        while n >= i and len(roman) < 2: 
            roman.append(symbols[i])
            n -= i 
            if n > 0: 
                roman.append(tens[len(roman) - 1])
                n //= 10     
            if n == 0: break

    if n > 0: 
        roman.append(symbols[n])
    
    result = ""
    for c in roman:
        result += c

    return result.lower()