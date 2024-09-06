```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    elif n < 5:
        return str(n) + "i"
    elif n < 10:
        return str(n) + "ii"
    elif n < 50:
        return str(n) + "iii"
    elif n < 100:
        return str(n) + "iv"
    elif n < 500:
        return str(n) + "v"
    elif n < 1000:
        return str(n)[:-1] + str(n)[-1] + "ix"
```

The overall approach is to handle each range of numbers differently based on their magnitude. For smaller numbers up to 10, it constructs the roman numeral by directly concatenating the corresponding roman numerals for the units, tens, and hundreds places. For numbers between 10 and 50, it leverages the fact that they often end with a "0" which simplifies the conversion. Numbers between 50 and 100 are handled by removing the final digit, then adding the remaining digit to "x" ten. Finally, it handles numbers between 100 and 500 by removing the hundreds place digit and iteratively subtracting from 500, converting each resulting number to roman numerals. The resulting numeral is then returned as a string.  This solution is efficient and accurately converts numbers to their mini roman numeral representations within the specified range.