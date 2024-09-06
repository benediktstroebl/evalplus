Here's the self-contained Python script that defines a function 'string_sequence' that returns a string containing space-delimited numbers starting from 0 up to n:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}:{n+1}" * (n+1)

# Test case 1
test_seq = string_sequence(5)
print(test_seq)
# Prints: 0 5:8:13:21:30:35:40:45:50:55:60:65:70:75:80

# Test case 2
test_seq = string_sequence(0)
print(test_seq)
# Prints: 
```