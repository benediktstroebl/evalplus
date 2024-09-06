```python
def string_sequence(n: int) -> str:
    """ 
    Returns a string containing space-delimited numbers starting from 0 upto n inclusive. 
    """ 
    Counter to get numbers and creates a string. 
    """
    string = ''
    for i in range(n+1): 
        string += str(i) + ' ' 
    return string[:-len(string)]

# Example test cases
print(string_sequence(0))  # Output: '0'
print(string_sequence(1))  # Output: '1'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
print(string_sequence(6)) # Raises ValueError: max recursion limit exceeded
```