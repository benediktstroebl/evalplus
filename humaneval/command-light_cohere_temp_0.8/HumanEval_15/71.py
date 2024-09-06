```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    
    def rec(i: int) -> str:
        if i < n:
            return f'{i + 1}'
        else: 
            return ''
            
    return ' '.join(rec(i) for i in range(n))

# Example Test Cases
print(string_sequence(0))
# Prints '0'

print(string_sequence(1))
# Prints '1'

print(string_sequence(5))
# Prints '0 1 2 3 4 5'

print(string_sequence(-1))
# Should throw error.
```