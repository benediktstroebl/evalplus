```python
def string_sequence(n: int) -> str:
    """ 
    Return a string containing space-delimited numbers starting from 0 upto n inclusive. 
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return f"0 {n}"

def test_string_sequence():
    assert string_sequence(0) == '0', "Test case 1 failed"
    assert string_sequence(5) == '0 5', "Test case 2 failed"
    assert string_sequence(10) == '0 9 8 7 6 5', "Test case 3 failed"
    assert string_sequence(1) == '1', "Test case 4 failed"
    return "Pass"

# Test the function
print(test_string_sequence())
 ```