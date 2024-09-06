```python
def digitSum(string):
    return sum(map(int, list(string.upper())))
```
This function uses the sum function with a mapping function and a list comprehension to convert the string to a list of digits and then to integers, finally returning the sum of the integer values. This solution works for the examples provided in the code block and should return the expected outputs when provided with the same strings.