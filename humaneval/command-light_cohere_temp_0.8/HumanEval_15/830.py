```python
def string_sequence(n: int) -> str:
    if not n:
        raise ValueError("Input cannot be zero.")
    elif n < 0:
        raise ValueError("Input must be non-negative.")

    string_sequence_ = ['0']
    for i in range(1, n + 1):
        string_sequence_.append(str(i))

    return ' '.join(string_sequence)

# Test cases
test_string_sequence = string_sequence(5)
print(test_string_sequence)

test_string_sequence = string_sequence(0)
print(test_string_sequence)

test_string_sequence = string_sequence(-5)
print(test_string_sequence)

test_string_sequence = string_sequence(10)
print(test_string_sequence)
```