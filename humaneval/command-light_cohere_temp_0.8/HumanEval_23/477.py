```python
def strlen(string: str) -> int:
    """ Returns length of given string """
    return len(string)

# Testing the function
>>> strlen('') # This should return 0
#=> len('') == 0
True
>>> strlen('abc') 
# This should return 3
#=> len('abc') == 3
True
```  This code defines a function strlen that calculates the length of a given string. The function uses the string parameter and returns an integer value of the length of the string using the built-in function len(). fact that returns the length of a given string. It also passes the all the expected test for the function, which returns the length of the empty string '' as 0 and the length of the string 'abc' as 3.