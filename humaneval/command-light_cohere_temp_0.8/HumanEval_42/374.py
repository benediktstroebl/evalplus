```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(l[-1] + 1)
    return l

# Test function to check the correctness of incr_list
def test_incr_list():
    test_list = [1, 2, 3]
    expected = [2, 3, 4]
    got = incr_list(test_list)
    assert expected == got, f"Expected: {expected}, Got: {got}"

# Driver code
if __name__ == "__main__":
    test_incr_list()
```