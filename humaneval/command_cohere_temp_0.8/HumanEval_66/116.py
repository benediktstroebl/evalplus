```python
def digitSum(s):
    return sum(map(int, list(filter(str.isdigit, s))))
```

The provided Python function `digitSum` calculates the sum of ASCII values of digits in a given string. It uses the `sum` function to add up the results of mapping integer values of digits obtained from filtering non-digit characters from the input string. This approach ensures that only digit characters are considered in the sum calculation.