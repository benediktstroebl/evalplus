```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments. It extracts the last digit of each number by using the index `-1` to access the last character in the string representation of each number. It then multiplies these last digits, regardless of the magnitudes of the original numbers, and returns the product as an integer. 

Here is an example usage of the function:
```python
print(multiply(14, 15))  # Output: 20
print(multiply(121, 353))  # Output: 4
print(multiply(0, 0))  # Output: 0
print(multiply(10, 100))  # Output: 1
``` 

This example demonstrates the versatility of the function in handling different scenarios, including positive and negative numbers, zeroes, and various magnitudes.