Here is a self-contained Python script that defines a function `strlen` which calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case 1:
def test_strlen():
    assert strlen('') == 0 

# Test case 2:
def test_strlen2():
    assert strlen('abc') == 3 

# Test case 3:
test_strlen() # Test automatically executed when this script is run 

# Expected Output:
# True
``` 
This script provides a self-contained solution and test cases for the given problem.