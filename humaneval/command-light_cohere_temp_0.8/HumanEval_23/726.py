Here is a self-contained Python script that defines a function strlen that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    return len(string)

# Test cases
string1 = ""
assert strlen(string1) == 0

string2 = "abc"
assert strlen(string2) == 3

string3 = "hello world"
assert strlen(string3) == 11

# Main function call
print(strlen(""))
``` 
This script defines a function `strlen` that takes a string as input and returns its length using the built-in function `len()`. The test cases are also provided to ensure the function's correctness.  The main function call is also shown to work correctly.