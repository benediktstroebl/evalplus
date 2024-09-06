```python
def digitSum(string):
    return sum(map(int, list(string.upper())))
```
This function uses the sum function with a mapping function and a list comprehension to calculate the sum of the ASCII values of all digits in the string, considering the upper case only.