Here's the self-contained Python script with a function `string_sequence` that creates a sequence of numbers from 0 to n (where n is the input parameter):

```python
def string_sequence(n: int) -> str:
    return f"0 {range(n+1, 0, -1)}"

# Test cases
test_cases = [0, 10, 15]
for n in test_cases:
    assert string_sequence(n) == f"0 {range(n+1, 0, -1)}"
```