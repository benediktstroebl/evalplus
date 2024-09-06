```python
def digitSum(s):
    return sum(map(int, list(filter(str.isdigit, s))))
```

The function `digitSum` uses the sum function to calculate the sum of the digits in the string. The map function transforms each character in the string to its corresponding integer value. The filter function filters out the non-digit characters from the string, leaving only digits. 

The code is self-contained and can be executed directly to test it against the given examples. It relies on standard built-in libraries, so it should work in any Python environment that supports markdown code blocks.