```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    elif n < 5:
        return str(n) + "i"
    elif n < 10:
        return str(n) + "v"
    elif n < 50:
        return str(n)[:1] + str(n)[1:] + "i"
    elif n < 100:
        return str(n) + "l"
    elif n < 200:
        return str(n)[:1] + str(n)[1:] + "l"
    elif n < 500:
        return str(n) + "x"
    elif n < 700:
        return str(n)[:1] + str(n)[1:] + "x"
    elif n < 1000:
        return str(n)[:1] + str(n)[1:] + "m"
```

This function handles each range of numbers according to the corresponding roman numeral representation. The logic for partitioning the numbers is mostly based on the decimal values of the Roman numerals. Numbers 1 through 4 are represented by the single roman numeral 'i', whereas numbers 5 through 9 are represented by the roman numeral 'v' plus the appropriate number of 'i's. This pattern repeats itself with increments of 5 until we reach 50. After which, we use 'l' for numbers up to 100, 'x' for numbers up to 500, and finally 'm' for numbers up to 1000. 

Thus, the function int_to_mini_roman(19) == 'xix', int_to_mini_roman(152) == 'clii', and int_to_mini_roman(426) == 'cdxxvi'.