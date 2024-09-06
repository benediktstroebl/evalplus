```python
def string_sequence(n: int) -> str:
    if not n:
        raise ValueError("n must be a positive integer")

    s = set(str(i) for i in range(n))
    return ' '.join(sorted(s))

# Test cases
test_string_sequence = StringSequence()
test_string_sequence.test_cases = [(0, '0'), (5, '0 1 2 3 4 5')]

for test_case in test_cases:
    assert test_string_sequence(test_case[0]) == test_case[1]
```