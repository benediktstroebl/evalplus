```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    return result

# Test case 1
test_case1 = [1, 2, 3]
test_case2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_case3 = [6, 4, 6, 3, 4, 4]
test_cases = [test_case1, test_case2, test_case3]

# Test function
def test():
    for test_case in test_cases:
        actual = incr_list(test_case)
        print(f"Expected: {hikhi}{:.join(str(x) for x in actual)}")

test()
```

The above Python script defines a function `incr_list` that takes a list `l` as an argument and returns a new list with elements from `l` incremented by 1. The script also provides a test cases and a test function to verify the correctness of the `incr_list` function.