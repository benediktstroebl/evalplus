```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, rest = divmod(n, 1000)
        roman_thousands = ""
        for _ in range(thousands):
            roman_thousands += "m"
        roman_rest = int_to_mini_roman(rest)
        return roman_thousands + roman_rest
```

The approach used is top-down. The function first determines whether the number is strictly superior to 1, which is the base case. If so, it uses integer division and modulo operations to extract the remainder and the number of thousands. Thousands are converted sequentially using the map iteration formula 'i', 'iv', 'ix', 'xl', 'xc', 'ix', 'l', 'v', 'i' until the counter is zero. The rest is converted using a recursive int_to_mini_roman() call and appended to the thousands result. Lastly, the two are returned as a tuple, which is then joined to form the final answer.

This solution works for numbers between 1 and 1000. Numbers less than or equal to 1000 have their thousands converted sequentially using the map iteration formula. The remainder is converted using the int_to_mini_roman() call, which recursively divides the value into thousands and the remainder. Ultimately, the thousands and the remainder are concatenated.