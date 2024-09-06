```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(l[-1] + 1)
    return l

#Test cases
test_incr_list = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [None, 10],
    [1, 2, 3, 4, 5]
]

def test_incr_list_func(test_cases):
    """
    Test suite for the incr_list function."""
    for test_case in test_cases:
        if isinstance(test_case, list):
            l = list(test_case)
            expected = [i+1 for i in l]
            got = incr_list(l)
            assert list(got) == expected, f"AssertionError: {got} != {expected}"
        return_value

#Main program
if __name__ == "__main__":
    test_incr_list_func(test_incr_list)
    print("All tests passed!")
```