```python
def digitSum(string):
    return sum(map(int, list(string.upper())))
```
This function uses the sum function to add up the integers represented by the digits in the string, and the map function to convert the characters in the string to integers. The map function applies the int function to each character in the string. The final result is the sum of the ASCII values of the upper-case characters in the string.