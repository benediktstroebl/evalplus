```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputs."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers as input and extracts the unit digits of both numbers. It does this by using the `int()` and `str()` functions to convert the numbers to strings and then access the last characters using `[-1]`. These unit digits are multiplied together using basic arithmetic operations, and the resulting product is returned as an integer. 

Let's assume the following call to the function: `multiply(452, 123)`
1. For the first parameter `452`, the call to `int(str(452)[-1])` becomes `int('2', base=10)`, which returns the integer `2`. 
2. For the second parameter `123`, the call to `int(str(123)[-1])` is `int('3', base=10)`, resulting in the integer `3`. 
3. The final result is the product of these two unit digits, `2 * 3 = 6`. 

Therefore, the function returns `6`, which is the product of the unit digits of the two input numbers.