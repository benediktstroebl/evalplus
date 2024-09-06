```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    assert(all(x >= 0 for x in result)), "Invalid: Negative value in result list."
    assert(len(result) == n), "Invalid: Length of result does not match input list."
    return result
``` 
Do you need any further assistance with this problem?