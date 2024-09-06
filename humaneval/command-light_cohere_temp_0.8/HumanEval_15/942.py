```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + str_sequence(n - 1) + "}"

def str_sequence(n: int) -> str:
    return ["".join(str(i)) for i in range(n + 1)]

# Test cases
test_seq = [
    assert string_sequence(0) == '0',
    assert string_sequence(1) == '1',
    assert string_sequence(5) == '0 1 2 3 4 5'
]
```