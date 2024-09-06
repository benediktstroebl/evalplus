```python
def digitSum(s):
    return sum(map(int, s.upper()))
```
This function uses the `sum()` function to add up the results of mapping the `int` function to each character in the string `s`. The `int` function converts each character in the string to its corresponding ASCII integer value. The `upper()` method is used to ensure that the ASCII codes of only the upper case characters are considered.