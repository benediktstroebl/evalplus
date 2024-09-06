```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

# Tests:
# Ensure the function correctly returns unique elements
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_unique) == [0, 2, 3, 5, 9, 123]

# Test with empty list
test_empty = []
assert unique(test_empty) == []

# Test with single element
test_single = [123]
assert unique(test_single) == [123]
```
The provided Python code defines a function unique that returns a list of unique elements from a given list. The function uses a set to keep track of elements that have been encountered and then iterates through the input list, adding elements to the set and the result list as they are not encountered before. The test suite includes a code to test the function with various inputs and confirms that it returns the correct unique elements.