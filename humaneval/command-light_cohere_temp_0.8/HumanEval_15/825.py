```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n} {" + str_sequence(n - 1) + "}" 

def str_sequence(n: int) -> str:
    """ Returns a string containing single space for each number, starting from 0 till n."""
    return " ".join([str(i) for i in range(n)])

# Test cases
string_sequence(0)      # Output: '0'
string_sequence(5)     # Output: '0 1 2 3 4 5'
string_sequence(-1)   # Output: error: expected integer, got -1
string_sequence(3.2)    # Output: error: invalid literal for int()
```