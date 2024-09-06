```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test cases
l = [1, 2, 3]
test_result = incr_list(l)
print("Test 1 result:", test_result)

l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = incr_list(l)
print("Test 2 result:", test_result)

l = [None, 100]
try:
    incr_list(l)
except TypeError:
    print("Exception occurred")

```
The function incr_list returns a new list with elements incremented by 1. Test cases are run this specific values and verify the function's output. You can use this many in markdown code blocks in your code to explain your code and its purpose to others. This method is the useful for creating clean and readable code, and makes it easier for others to understand what your code is doing.