```python
def digitSum(string):
    return sum(map(int, list(filter(str.isdigit, string))))
```

The idea is to filter out the non-digit characters from the string, convert them into numbers, and then sum them up.

This approach leverages Python's str.isdigit method to filter out only the digit characters from the original string. The filtered characters are then converted into integers using map(int, ...), and these integers are summed up using the built-in sum function. 

This efficiently computes the desired sum of upper-case ASCII codes of the digits in the input string.