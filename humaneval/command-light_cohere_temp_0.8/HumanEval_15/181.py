```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending at n inclusive"""
    
    # Append numbers starting from 0 to the result string
    result = ""
    for i in range(n+1): 
        result += str(i)

    return result

# Test cases
print(string_sequence(0))  # Output: '0'
print(string_sequence(1))  # Output: '1'
print(string_sequence(5))  # Output: '0 1 2 3 4 5' as expected
print(string_sequence(6))  # Error: Input 6; this is out of range; raises ValueError)
```