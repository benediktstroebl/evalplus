```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [i + 1 for i in l]
    return new_list

# Test the function with a list of values
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_list)

# Print the result and compare it with the expected output
print("Result:", result)
print("Expected:", [6, 4, 6, 3, 4, 4, 10, 1, 124])

if result == test_list:
    print("Test passed!")
else:
    print("Test failed.")
```
The code defines a function incr_list that takes a list l as input and returns a new list with elements from input list incremented by 1. 

The code then creates a test list with values and calls the incr_list function with the test list. Finally, it compares the result with the expected output and reports the test status accordingly.