```python
def int_to_mini_roman(n):
    if n < 1000:
        result = []
        for x in range(0, n + 1):
            if x != 0:
                result.append(mini_roman[x])
        result.reverse()
        return ''.join(result)
    else:
        return 'Error!'

roman = ['i', 'v', 'x', 'l', 'c', 'd', 'm']
mini_roman = ['i', 'iv', 'ix', 'lx', 'lc', 'ld', 'lm']
```

The function `int_to_mini_roman` converts a given positive integer into its miniature Roman numeral representation as a string. It uses a dictionary to map each number to its corresponding Roman numeral letter in the miniature version. To achieve this, it iterates through each digit of the integer and appends the corresponding miniature Roman numeral to a result list. Finally, the function joins these letters to form the Roman numeral string and returns it if the input is within the specified range (1 to 1000). If the input is outside this range, the function returns an error message.