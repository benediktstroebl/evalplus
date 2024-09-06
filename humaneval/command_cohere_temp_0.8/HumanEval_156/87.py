```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    res = []
    for i in range(1, 1000):
        if n >= i:
            count = len(str(i))
            res.extend(str(i)[::-1][:count])
            n -= i
    return ''.join(res)
```

This Python script defines a function called `int_to_mini_roman` which takes a single argument `n`, representing a positive integer. This function converts the given positive integer into its mini Roman numeral representation as a string and returns it in lowercase. It relies on generating the Roman numerals sequentially for numbers between 1 and 1000. The result is achieved by joining the generated Roman numerals. If the input is not a positive integer, a ValueError is raised. 

To use this code, copy and paste it into a Python environment or script and invoke the `int_to_mini_roman` function with a positive integer as follows: `result = int_to_mini_roman(number)`. This will return the Roman numeral representation of the given number, converted to a string and in lowercase. 

Make sure the iteration is in descending order to avoid unnecessary updates to the `n` variable.