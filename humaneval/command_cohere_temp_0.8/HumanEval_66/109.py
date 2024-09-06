```python
def digitSum(string):
    return sum(map(int, list(string.upper())))
```
This function uses the sum function with the map function to convert the characters of the string to their numeric value, and then returns the total. This works because the ASCII codes of uppercase characters range from 65 (A) to 90 (Z), producing the desired result.