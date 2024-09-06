```python
def digitSum(s):
    return sum(map(int, list(filter(str.isdigit, s))))
```

The provided Python function `digitSum` calculates the sum of ASCII values of digits in a given string `s`. It first maps each character in the string to its corresponding integer value using the `int` function. The resulting integers are then filtered using `str.isdigit` to keep only those characters that represent digits. Finally, the sum of the filtered integer values is returned, providing a straightforward solution to the task as described in the prompt.