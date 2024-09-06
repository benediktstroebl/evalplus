```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments and returns the product of the unit digits of each number. The unit digit is the digit at the far right of a number. For example, in the input `148`, the unit digit is `8`.

The function uses the `-1` indexing convention to retrieve these unit digits, leveraging the str[index] syntax to extract the last character of each input number. It then uses the `int()` function to convert these extracted characters back into integers for the actual multiplication. 

Let's go through some examples to understand the function's behavior:
1. `multiply(148, 412)` -> `16` 
2. `multiply(19, 28)` -> `72` 
3. `multiply(2020, 1851)` -> `0` 
4. `multiply(14, -15)` -> `20` 

The function efficiently computes the product of unit digits, providing the expected output for each test case.