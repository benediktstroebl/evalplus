```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments and returns the product of the unit digits of each number. The unit digit is the last digit of a number. This is achieved by using the built-in function `str` to convert both input integers to strings, accessing the last digit of each string using `str(a)[-1]` and `str(b)[-1]`, and then multiplying these extracted digits together to obtain the final result. 

Let's apply this function to a test scenario: multiply(19, 28)
1. The function str(19) = '19'
2. The function str(28) = '28'
3. The last digit of 19 is 9 and the last digit of 28 is 8.
4. 9 * 8 = 72

Therefore, the result of multiply(19, 28) is 72, which accurately solves the problem.