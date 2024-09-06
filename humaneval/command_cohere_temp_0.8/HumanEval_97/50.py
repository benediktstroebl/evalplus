```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The code directly computes the product of the unit digits, `dig1` and `dig2`, to obtain a result that is also a unit digit, which is then returned.

This approach follows the fundamentals of computing the product of two integers, where the units or digits are multiplied first, going from right to left, and the result is then simplified by successive multiplication and carrying (also known as long multiplication). In this case, since we're focusing on the unit digits only, the result will always be a single digit, making the modulo operation for simplification redundant. Thus, the solution directly computes the product of the unit digits. 

The provided examples in the prompt are all within the function's comment section, and the expected output is mentioned alongside them. The function's expected behavior is to return the product of the unit digits of the two input numbers, considering the input is always valid.  The function can be tested with other sets of numbers to verify its behavior further.