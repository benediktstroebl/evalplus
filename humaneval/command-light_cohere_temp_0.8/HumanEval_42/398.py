```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    return result

# Test suite for incr_list function
    tests = [
        (["List with [1, 2, 3, 4]"], incr_list),
        (["List with [5, 3, 5, 2, 3, 3, 9, 0, 123]"], incr_list),
        (["List with mixed elements [1, 2, 7, 5]"], incr_list),
        (["[]"], incr_list),
        (["a"], incr_list),
        (["aa"], incr_list),
        (["abc"], incr_list),
        (["abcde"], incr_list),
        (["a", "b", "c"], incr_list),
        (["aa", "bb", "cc"], incr_list),
        (["a", "bb", "a", "a", "bb", "a"], incr_list),
        (["aa", "bb", "a", "b", "c", "a"], incr_list),
    ]

    for test_case, func in tests:
        l = list(test_case)
        result = func(l)
        assert l == result, f"Error in test case {test_case} - Expected {l} but got {result}"
```
This Python code defines a function incr_list that incrementally every element in a given list by 1. It also includes a test suite with various input lists and expected outputs, using the assert statement to verify the correctness of the incr_list function.