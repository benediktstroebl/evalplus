```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [i + 1 for i in l]
    return new_list

# Test case 1
test_case1 = [1, 2, 3]
test_result1 = incr_list(test_case1)
assert test_result1 == [2, 3, 4]

# Test case 2
test_case2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result2 = incr_list(test_case2)
assert test_result2 == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3 (Should raise IndexError)
test_case3 = [1, 2, 3, 4, 5, 6]
try:
    test_result3 = incr_list(test_case3)
except IndexError:
    print("Test case 3 passed.")
else:
    print("Test case 3 did not pass.")
```
The code defines the incr_list function, which takes a list l as input and returns a new list with elements incremented by 1. The test cases ensure that the script works as expected.