```python
def digitSum(s):
    return sum(map(int, s.upper()))
```
This Python function uses the `sum()` function to add up the integers represented by the digits in the string. The `map()` function is used to convert the characters in the string to integers, with `s.upper()` ensuring that only the upper-case characters are considered. This approach directly computes the sum of the ASCII values of the upper-case characters only, as required by the problem.