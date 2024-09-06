Here is a self-contained Python script that defines a function `strlen` to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
string1 = ""
string2 = "abc"

print(strlen(string1))  # Output: 0
print(strlen(string2))  # Output: 3

string3 = "hello world"
print(strlen(string3))  # Output: 11

```

This script defines a function `strlen` that calculates the length of a given string. The function uses the simple Python `len()` function to get the length of the string. The function is self-contained and passes all the corresponding tests without using any external functions.