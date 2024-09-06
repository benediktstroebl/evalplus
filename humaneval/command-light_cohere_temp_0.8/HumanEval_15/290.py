```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{' ' * (n - 1)} 5"

# Test case 1
test_seq = string_sequence(5)
print(test_seq)
# Output: 0 5 8 10

# Test case 2
test_seq = string_sequence(0)
print(test_seq)
# Output:  0 

# Test case 3
test_seq = string_sequence(-5)
print(test_seq)
# Output:  0  99

# Test case 4
test_seq = string_sequence(10)
print(test_seq)
# Output: 0 9 19 27 41 49  65 83 91 109 115 121 137 149 

# Test case 5
test_seq = string_sequence(0)
test_seq[:- shortest_len]
print(test_seq)
# Output:  0 
```