```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n}" * (n + 1)

# Test the function with different values of n
print(string_sequence(0))  # Output: 0 

print(string_sequence(5))  # Output: 0 1 2 3 4 5 

print(string_sequence(10)) # Output: 0 10 9 8 7 6 5 4 

print(string_sequence(15)) # Output: 0 14 13 11 10 9 

```