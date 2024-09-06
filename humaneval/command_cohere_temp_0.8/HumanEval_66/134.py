```python
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```
This function uses the sum function's ability to iterate over a string and the ord function to get the ASCII value for each character. The filter condition is specified using the isupper function. The function then returns the sum of the uppercase characters' ASCII codes. The algorithm's efficiency can handle even longer strings without impacting performance.  This solution's uniqueness ensures it complies with the problem statement.