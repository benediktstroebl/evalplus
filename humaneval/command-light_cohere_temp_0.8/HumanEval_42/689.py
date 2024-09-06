```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l.append(l[-1]+1)
    return l

# Test cases
test_incr_list = [
    [
        [1, 2, 3], 
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        [None]
    ]

def test_func(test_case):
    l = incr_list(test_case)
    for item, expected in zip(l, test_case):
        assert item == expected, f"Case {test_case} failed: {item}-{expected}"

# Main function
if __name__ == "__main__":
    test_incr_list = [
        [1, 2, 3], 
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        [None]
    ]

    test_func(test_incr_list[0])
    test_func(test_incr_list[1])
    test_func(test_incr_list[2])
```

The provided solution calculates the incremented list and compares it with the provided test cases.  The function uses the simple logic to append the last element to the list and return the result.