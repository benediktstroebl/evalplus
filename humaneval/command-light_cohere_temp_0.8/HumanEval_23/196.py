Certainly, here's a self-contained Python function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """Return length of given string"""
    return len(string)

# Test case 1:
print(strlen('')) 

# Test case 2:
print(strlen('abc')) 

# Test case 3:
string1 = 'hello world'
print(strlen(string1)) 

# Test case 4:
string2 = ''
print(strlen(string2)) 
```

This function is designed to calculate the length of any given string, and it passes all the test cases provided.