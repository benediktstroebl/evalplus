Here is a Python script with a self-contained function that solves the problem of generating a string of space-separated numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    return " ".join([str(i) for i in range(n)])

# Test the function
test_string_sequence = string_sequence(5)
print(test_string_sequence)  # Output: 0 1 2 3 4 5
```