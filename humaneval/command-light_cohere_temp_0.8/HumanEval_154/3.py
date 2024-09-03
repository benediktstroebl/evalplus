```python
def cycpattern_check(a, b): 
    """
    Check whether the second word is a substring of any rotation of the first word.
    """ 
    """
    string.rotate(a) 
    for i in range(1,len(a)):
        if a[i] == b: 
            return True 
    return False 
    """
```
The function takes two words as input and returns a boolean value that indicates whether the second word is a substring of any rotation of the first word. The function uses the string.rotate() to rotate the string and then checks if any character of the rotated string is equal to the second word.