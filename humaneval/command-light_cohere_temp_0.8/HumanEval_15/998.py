```python
def string_sequence(n: int) -> str:
    """ 
    Return a string containing space-delimited numbers starting from 0 upto n inclusive. 
    """
    string_sequence(0) 
    """ return '0'  # earliest possible number
    """
    return "".join(range(0, n + 1))

def test_string_sequence():
    """ 
    Function to test the string_sequence function
    """
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(0) == '0'
    assert string_sequence(10) == '9' 

# Test cases are added below this function

# test_string_sequence()
```