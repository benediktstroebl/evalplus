Here's the self-contained Python function that generates a sequence of numbers:
```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2}"

# Test cases
test_sequence = []
test_sequence.append(string_sequence(0))
test_sequence.append(string_sequence(5))
test_sequence.append(string_sequence(10))
test_sequence.append(string_sequence(5))

# Prints the test case output
print(*test_sequence.show(test_sequence))
```