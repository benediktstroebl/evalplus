```python
def digitSum(string):
    return sum(ord(char) for char in string if char.isupper())
```
The provided Python code defines a function called digitSum that takes a string as its input parameter, and its purpose is to compute the sum of the ASCII values of all uppercase characters present in the input string. Within the function, it uses a list comprehension accompanied by the sum function to aggregate the numerical values of these uppercase characters, as indicated by the condition char.isupper(), which checks if a character is uppercase. This effectively calculates the total of the ASCII values corresponding to those uppercase characters and returns the resultant sum as the function's output.