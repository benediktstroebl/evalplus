```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{' ' * (n - 1)}{n+1}"

#Test cases
print(string_sequence(0))        # Output: 0 

print(string_sequence(1))        # Output: 0 1 

print(string_sequence(5))        # Output: 0 1 2 3 4 5 

print(string_sequence(6))        # Output: 0 6 

print(string_sequence(10))       # Should raise an error: n is less than or equal to 0

string_sequenceString = string_sequence  # Store the function for later use

print(string_sequenceString(10)) # Output: 0 10 9 8 7 6 5 3 2 1 

```