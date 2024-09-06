```python
def multiply(a, b):
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers as input and returns the product of their unit digits, where the unit digit is the digit immediately to the right of the decimal point. This is achieved by using the `-1` index on the string representation of each number to access the unit digit, which is then converted back to an integer for the multiplication. The resulting output is the product of these two digits. 

This approach ensures that the function will work for both positive and negative numbers, as well as any valid input that has a length of at least one character so that it will not cause a `ValueError` when accessing the unit digit. 

Note that this assumes that the input is valid and that the integers are expressed in base 10. 

This approach could potentially encounter errors with non-integer inputs, illegal literal characters, or numbers expressed in other bases. However, given the assumption that the input is always valid, these potential issues are outside the scope of this problem.