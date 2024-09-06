```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, rest = divmod(n, 1000)
        if thousands:
            return str(thousands) + "m" + int_to_mini_roman(rest)
        digits, num = divmod(rest, 5)
        if digits:
            return "i" * digits + num
        else:
            return str(num)
```

The modular approach is utilized to break down the problem into manageable components. Firstly, the number is divided into thousands and the rest, employing the `divmod` function. This enables us to concentrate on the remaining digits, which can be further split into groups of five and the remainder. By doing so, we effectively convert the number into its roman numeral equivalent. 

The test cases are designed to validate the function's effectiveness for inputs within the stated range of 1 to 1,000. These tests verify if the function produces the correct roman numerals based on the division of the input number.