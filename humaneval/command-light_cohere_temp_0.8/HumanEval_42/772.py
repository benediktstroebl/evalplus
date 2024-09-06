```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [i + 1 for i in l]
    assert len(result) == n
    assert all(result) == [i + 1 for i in l]
    return result

# Example usage
input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(input_list)
print(result)
```