```python
def digitSum(s):
    return sum(map(int, s.upper()))
```
This function uses the `sum()` function to add up the integers represented by the digits in the string. The `map()` function is used to convert the characters in the string to integers, and the `upper()` function is used to ensure that the characters are in uppercase. This is done to make sure that the digit sum is calculated corresponding to the upper characters in the provided string as stated in the task.