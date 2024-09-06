```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n 

# Test the function with different values of n 
test_string_sequence = StringSequence()
test_string_sequence.py  # assert test_string_sequence(0) == '0'
test_string_sequence.py  # assert test_string_sequence(5) == '0 5 10 15 20 25'
```