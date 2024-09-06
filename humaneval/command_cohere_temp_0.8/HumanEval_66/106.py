```python
def digitSum(s):
    return sum(map(int, s.upper()))
```
This Python function uses the sum function in conjunction with the map function to convert each character in the input string to its ASCII value and returns the sum of those values. The map function applies the int function to each character in the string, converting it to a numeric representation. The result is the sum of the ASCII values of the digits present in the string.