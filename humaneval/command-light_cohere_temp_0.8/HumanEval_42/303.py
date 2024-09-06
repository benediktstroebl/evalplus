```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [x + 1 for x in l]

# Test the function with a sample input
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = incr_list(test_incr_list)

# Print the expected result and the actual result
print("Expected:", test_incr_list)
print("Actual:", test_result)

if test_result == test_incr_list:
    print("Test passed.")
else:
    print("Test failed.")
```
This script defines a function incr_list that takes a list l as input and returns a new list with elements incremented by 1. It then tests this function with a sample input list and compares the result against the expected output, and based on the result, it will print the appropriate success or failure message.