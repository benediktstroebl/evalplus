```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc', []], [10, None, True, (1), [1, 2]])

test_cases = {
    'input': test_values,
    'expected': [['a', 3, 5], [1, 2, 'abc', []], [10, None, True, (1), [1, 2]])
}

for key, (input_, expected) in test_cases.items():
    print(f(input_) == expected))
```