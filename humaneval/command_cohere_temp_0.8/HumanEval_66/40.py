```python
def digitSum(s):
    return sum(map(int, s.upper()))
```
This function uses the sum function to add up the integers represented by the digits in the string, and the map function to convert the string to a list of integers. The upper() method is applied to the string to ensure that only the digits are considered, regardless of the letter case.