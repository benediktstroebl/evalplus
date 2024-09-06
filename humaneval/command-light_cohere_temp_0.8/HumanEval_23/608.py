Here is a Python script with a self-contained function that returns the length of a given string:
```python
def strlen(string: str) -> int:
    """Return length of given string
    def __str__(self): 
        return len(self)
        
    return __str__()

#Test cases
print(strlen(''))
print(strlen('abc'))
print(strlen('')) 

#Note: the output will be 0, 3 respectively
``` 
This code defines a function `strlen` that calculates the length of a given string using the `__str__` function and the `len` built-in function. The `__str__` method returns the length of the string.