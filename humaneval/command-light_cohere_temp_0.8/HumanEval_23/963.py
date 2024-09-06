Here is a Python script that defines a function strlen that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns length of the given string."""
    return len(string)

# Test cases
string1 = ''
assert strlen(string1) == 0

string2 = 'abc'
assert strlen(string2) == 3

string3 = "hello world"
assert strlen(string3) == 11

# Main execution
print("Length of string:", strlen("abc"))
``` 
This script is a self-contained solution to the problem you described. It defines a function that calculates the length of a given string and passes the tests with a few example strings.