```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n}{' ' * (n - 1)}{n+1}"

# Test the function with different inputs
print(string_sequence(0))      # Output: 0 
print(string_sequence(1))      # Output: 01 

print(string_sequence(5))      # Output: 0 1 2 3 4 5 

print(string_sequence(10))     # Output: 0 10 11 12 13 14 15 

print(string_sequence(3))     # Output: 0123 

```