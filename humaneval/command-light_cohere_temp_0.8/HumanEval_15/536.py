```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n}..."join(str(i+1) for i in range(n))

if __name__ == "__main__":
    assert string_sequence(0) == '0', "Error: 0 not returning expected value"
    assert string_sequence(1) == '1', "Error: 1 not returning expected value"
    assert string_sequence(5) == '0 1 2 3 4 5', "Error: 5 not returning expected value"
    assert string_sequence(-1) == '0', "Error: Should handle negative value"
    assert string_sequence(100) == '00 100', "Error: Should handle large n"
```