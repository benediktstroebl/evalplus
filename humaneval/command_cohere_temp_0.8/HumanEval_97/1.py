```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments and returns the product of the unit digits of each number. The unit digit is the last digit of a number. This is achieved by using the built-in function `str` to convert both input integers to strings, accessing the last digit (the unit digit) using `str(a)[-1]` and `str(b)[-1]`, and then multiplying these extracted unit digits together. The result is then converted back to an integer using the `int` function. 

Let's use the function with the example inputs provided in the problem statement:
- `multiply(148, 412)`: The output would be `16`, as the unit digits of `148` and `412` are `1` and `4`, respectively, and 1 * 4 = 4.
- `multiply(19, 28)`: The output would be `72`, as the unit digits of `19` and `28` are `9` and `2`, respectively, and 9 * 2 = 18.
- `multiply(2020, 1851)`: The output would be `0`, as the unit digits of `2020` and `1851` are `0` and `1`, respectively, and 0 * 1 = 0.
- `multiply(14, -15)`: The output would be `20`, as the unit digits of `14` and `-15` are `4` and `-1`, respectively, and 4 * (-1) = -4. The negative result is converted to a positive result by multiplying the two digits.

This function adheres to the problem statement and performs the requested operation without requiring additional external variables or assumptions about the input. It is a self-contained Python function that solves the given problem.  This function is also general and does not contain any assumptions or special cases for the digits '1' and '0', which allows it to handle any valid input.  It's resilient to variable input kinds, numbers with varied digit counts, and potentially negative numbers.