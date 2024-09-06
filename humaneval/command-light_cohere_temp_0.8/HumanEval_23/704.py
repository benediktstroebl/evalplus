Here is a self-contained Python script that defines a function `strlen` to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case 1: empty string
print(strlen(""))  
# Output: 0

# Test case 2: abc as a string
print(strlen("abc"))  
# Output: 3
``` 
The `strlen` function takes a string as an argument and returns its length using the built-in function `len()`.  This provides a complete solution to the problem and does not require any external functions or modules for its implementation.