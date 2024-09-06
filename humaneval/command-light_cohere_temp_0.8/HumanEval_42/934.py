```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    assert len(result) == n, f"Result list has unexpected length {len(result)}, expected {n}"
    assert all(x == n - 1 for x in result), f"List was not filled with consecutive numbers starting from {n}"
    return result

# Example usage
my_list = [5, 3, 5, 2, 3, 3]
result_example = incr_list(my_list)
print(result_example)
```