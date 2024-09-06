```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l[:] = [x+1 for x in l]
    return l

# Test the function with different lists
test_list = [1, 2, 3]
test_list2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]

# Function call and print the result
result = incr_list(test_list)
print("Test 1 result:", result)
result = incr_list(test_list2)
print("Test 2 result:", result)
```
This Python code defines a function `incr_list` that incrementally the elements of a given list by 1. It then tests this function with two different lists and prints the results.