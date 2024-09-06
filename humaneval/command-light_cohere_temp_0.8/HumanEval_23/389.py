Here's a self-contained Python function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

#Test cases
string1 = ""
string2 = "abc"
string3 = "hello world"

print("Result for string1:", strlen(string1))
print("Result for string2:", strlen(string2))
print("Result for string3:", strlen(string3))
```
The code defines a `strlen` function that calculates the length of a given string using the `len()` function.  The purpose of this function is to find the length of any given string.