```python
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
```

The previously provided code defines the `int_to_mini_roman` function which converts an integer input into its mini roman numeral representation as a string. It applies the following logic:
- If the `number` is less than 1, it returns an empty string.
- It prepares three lists: `symbols` for single digits, `tens` for tens place digits, and `hundreds` for hundred's place digits.
- An empty string `roman` is initialized to hold the roman numerals.
- A loop iterates through the `symbols` list, generating roman numerals, it keeps subtracting values from `n` and appending digits to `roman`.
- After the loop, if `n` is still greater than 0, it adds the remaining value from `symbols` to `roman`. 
- Finally, another loop converts the roman numerals to a string and appends it to a string `result`. 

The resulting code is concise and efficient, providing a straightforward solution to the problem. It achieves this without importing any additional modules, making it a self-contained solution in the spirit of the prompt.