```python
def digitSum(s):
    return sum(map(int, list(filter(str.isdigit, s))))
```

The provided Python function `digitSum` calculates the sum of ASCII values of digits in a given string. It first uses the `filter` function with `str.isdigit` to extract all digit characters from the input string. Then, the `map` function converts these filtered characters to integers, and the `sum` function adds these integer values together. The resulting sum of ASCII codes represents the total value of upper-case characters in the input string.