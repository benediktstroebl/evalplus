```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    
    # Initialise the string to be returned 
    string = ""

    # Loop until we have filled the string
    for i in range(n + 1): 
        string += str(i)

    return string

# Test cases
print(string_sequence(0))       # Output: 0
print(string_sequence(3))       # Output: 03
print(string_sequence(10))      # Output: 0101010101
print(string_sequence(2))      # Output: 0011001100101
print(string_sequence(100))    # Output: 000000001111111111
```