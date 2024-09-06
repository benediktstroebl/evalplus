```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        hundreds, rem = divmod(n, 500)
        if hundreds > 0:
            return int_to_mini_roman(hundreds) + "c" + int_to_mini_roman(rem)
        else:
            tens, ones = divmod(rem, 5)
            if tens == 0:
                return int_to_mini_roman(ones)
            else:
                return int_to_mini_roman(tens) + int_to_mini_roman(ones)
```

The approach used here divides the problem into simpler parts, where each number is transformed into its roman numeral equivalent by relying on the properties that roman numerals follow. Firstly, hundreds are computed by dividing the given number by 500 and then int_to_mini_roman is recursively called on the result. This process continues until the number is small enough that it maps to a specific roman numeral. Ultimately, the tens and ones properties are used to build the roman numeral string. The condition hundreds > 0 ensures that the actual hundreds roman numeral is used.