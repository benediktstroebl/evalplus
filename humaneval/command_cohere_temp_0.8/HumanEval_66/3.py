```python
def digitSum(string):
    return sum(map(int, list(string.upper())))
```
This function uses the sum function to add up the integers represented by the digits in the string, and the map function to convert the characters of the string to integers. The map function applies the int function to each character in the string, and the resulting list of integers is summed up by the sum function. Note that the input string is converted to uppercase implicitly due to the uppercase() method invocation. This ensures that the ASCII codes of the digits are correctly calculated without considering the actual characters or their case.