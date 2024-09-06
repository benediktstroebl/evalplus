Here is a Python script that contains a self-contained function that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case 1
test_strlen = []
test_strlen.add((strlen(""), 0)
test_strlen.add((strlen("abc"), 3)
# Test case 2
test_strlen = [test_strlen[i] for i in range(len(test_strlen))]
# Print the test cases
print(test_strlen)
``` 
This code defines a function `strlen` that calculates the length of a given string. 
It takes a string parameter and returns the length of the string using the built-in function `len()`. importantly, the function is written in a way that it can be self-contained, and does not depend on any other functions or modules.