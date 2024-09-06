```python
def digitSum(s):
    return sum(map(int, list(filter(str.isdigit, s))))
```

The provided Python function `digitSum` calculates the sum of ASCII values of digits in a string. It first filters out digit characters using `str.isdigit`, converting them to integers with `map`, and then sums these integer values using `sum`. This results in the total of the numeric values of all digit characters in the input string.