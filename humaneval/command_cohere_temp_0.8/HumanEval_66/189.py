```python
def digitSum(s):
    return sum(map(int, s.upper()))
```
This function uses the sum function to add up the ASCII values of all digits in the string, and the map function to convert the digits of the string to integers. The result is the sum of the ASCII codes of the upper characters in the string. Basically, the function sums the ASCII values of all digits and returns the result.