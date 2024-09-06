```python
def strlen(string: str) -> int:
    """ Returns length of given string"""
    return len(string)

# Test cases
assertEqual(strlen(''),   0)
assertEqual(strlen('abc')), 3
assertEqual(strlen('']), 4)
assertEqual(strlen('abcde')), 5 )
```  This code defines a function `strlen` that calculates the length of a given string. 

The `test` cases ensure the function's correctness for different inputs.