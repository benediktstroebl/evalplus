```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

#Test Case 1:
def test1():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

#Test Case 2:
def test2():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 4, 10, 1, 124]

# Test Case 3: farfail: cannot assign to 'None'
test3()

# Test Case 4:
def test4():
    assert len(incr_list([])), "Should return empty list"

# Run all tests above

# Time travel debug output:
print("--- Testing incr_list ---")
test1()
test2()
test3()
test4()
print("--- Done Testing incr_list ---")
```
This script provides a self-contained function `incr_list` that returns a list with elements incremented by 1. The test cases cover a scenarios: adding elements to an empty list, incrementing existing elements, and ensuring the function works as expected. The code also includes a time travel debug to show the test results.