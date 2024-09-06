```python
def string_sequence(n: int) -> str:
    return f"0 {n}".format()

# Test case for the above function
test_str = string_sequence(5)
print(test_str)
# Output : 0 5 

test_str = string_sequence(0)
print(test_str)
# Output : 0 

test_str = string_sequence(-1)
print(test_str)
# Raises an error: ValueError
```