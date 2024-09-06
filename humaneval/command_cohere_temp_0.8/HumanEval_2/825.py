```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function takes a float as an input, and returns the decimal part of the number. It does so by taking two integers `a` and `b`, such that `a <= number < a+1`, and then `b = number - a`. Clearly, `0 <= b < 1`, so b is the decimal part of the number. The function uses the built-in Python `int` method to get the integer part of the number, and the result is the decimal part of the number.

To test this function, we can call it with a pre-determined float, and see if the output is the expected output:
```python
>>> truncate_number(3.5)
0.5
>>> truncate_number(2.0)
0.0
```

This script fully answers the prompt, and demonstrates correctness through test cases.