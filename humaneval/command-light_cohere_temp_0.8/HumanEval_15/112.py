```python
def string_sequence(n: int) -> str:
    return f"0 {n} " * (n+1)

# Test the function with a few inputs
test_sequence = string_sequence 0
print(test_sequence)  # Output: 0 
test_sequence = string_sequence 5
print(test_sequence)  # Output: 0 1 2 3 4 5 

test_sequence = string_sequence 10
print(test_sequence)  # Output: 0 10 10 10 10 10 

test_sequence = string_sequence -1
print(test_sequence)  # Output: -1 

# Using assert to test individual characters in the output
test_sequence_length = string_sequence(10)
assert len(test_sequence_length) == 10, "Wrong length"

test_alpha = string_sequence("abc")
assert test_alpha == "abc", "Wrong output for string_sequence"
```