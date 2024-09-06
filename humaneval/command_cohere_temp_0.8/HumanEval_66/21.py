```python
def digitSum(string):
    return sum(map(int, list(string.upper())))
```
This function uses the sum function to add up the results of mapping the int function to each character in the string. The mapfunction applies the int function to each character in the string, and the resulting list of digits is summed using the sum function. Note that the input string is converted to uppercase using the upper method, so that the sum is calculated based on the numeric value of the uppercase characters.