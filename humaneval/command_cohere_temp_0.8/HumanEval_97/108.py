```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments. It extracts the last digit of each number by accessing the last element of their string representations using `str(a)[-1]` and `str(b)[-1]`. These last digits are then multiplied together using the `int` function to ensure the result is also an integer, and the product is returned. 

Let's take some examples from the prompt to see how the function performs:
1. `multiply(148, 412)`— The last digit of '148' is '8', and the last digit of '412' is '2'. Thus, the function returns `8 * 2 = 16`.
2. `multiply(19, 28)`— The last digit of '19' is '9', and the last digit of '28' is '8'. Hence, the function returns `9 * 8 = 72`.
3. `multiply(2020, 1851)`— The last digit of '2020' is '0', and the last digit of '1851' is '1'. Consequently, the function returns `0 * 1 = 0`.
4. `multiply(14, -15)`— The last digit of '14' is '4', and the last digit of '-15' is '5'. Hence, the function returns `4 * 5 = 20`.

The function correctly calculates the product of the unit digits of the provided integers.