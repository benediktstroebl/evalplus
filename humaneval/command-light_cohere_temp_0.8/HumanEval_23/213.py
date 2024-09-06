```python
def strlen(string: str) -> int:
    """ Return length of given string
    Returns length of string.
    """ 
    if not string:
        raise ValueError("Input cannot be empty")
        
    return len(string)

#Test cases
assert strlen('') == 0
assert strlen('abc') == 3
try:
    strlen('')
    assert False
except ValueError as e:
    assert str(e) == 'Input cannot be empty'

# Example usage
print(strlen('abc'))
 ```