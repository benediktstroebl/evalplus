```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    for i in range(n):
        l[i] = l[i] + 1
    return l

# Test the function with a list of integers
test_list = [1, 2, 3]
result = incr_list(test_list)
print("Test 1 Result:", result)

# Test the function with a list of strings
test_str = ["abc", "def", "Hello"]
result = incr_list(test_str)
print("Test 2 Result:", result)

# Test the function with custom iterable
test_iter = ("a", "b", "c", "d", "e", "f", "g")
result = incr_list(test_iter)
print("Test 3 Result:", result)
```
The above Python script defines a function `incr_list` that takes a single argument `l`, which is an iterable (list, tuple, etc.), and returns a new list with elements from the original iterable incremented by 1. The function is then tested with three different cases: lists of integers, lists of strings, and a custom iterable.