```python
def digitSum(s):
    return sum(map(int, s.upper()))
```
This Python script defines a function called digitSum that takes a string as input and returns the sum of the ASCII codes of the upper case characters in the string. The function uses the sum function to add up the result of mapping the string to integers using the map function. The map function converts each upper case character in the string to its corresponding ASCII code, which is then added to the total sum. This is done for all upper case characters present in the string, and the result is returned as the output of the function.  This solution has an time complexity of O(n) as it takes the sum of the characters of the string.