```python
def digitSum(string):
    return sum(ord(char) for char in string if char.isupper())
```
The `digitSum` function iterates through each character in the string using a list comprehension. It only includes the characters in the sum calculation if they are uppercase letters (`char.isupper()`). The `ord()` function converts each character to its ASCII code, and `sum()` adds up all these numerical values to provide the total sum of upper characters' ASCII codes.