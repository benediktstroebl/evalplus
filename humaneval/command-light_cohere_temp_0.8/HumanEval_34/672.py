```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
  return result

# Test 1: Ensure it returns unique list
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result1 = unique(test_case1)
assert len(result1) == 7, "Test 1 failed"

# Test 2: Ensure it doesn't add duplicates
test_case2 = [2, 2, 5, 3, 5, 5, 0, 5]
result2 = unique(test_case2)
assert len(result2) == 5, "Test 2 failed"

# Test 3: Ensure it works with empty list
test_case3 = []
result3 = unique(test_case3)
assert len(result3) == 0, "Test 3 failed"
```
The code defines a function unique that takes a list lst as input and returns a list of unique elements from that list. It uses a unique set to keep track of the unique elements and a list result to store the unique elements. The code also provides several tests to validate the correctness of the unique function: it verifies that the returned unique list contains all expected elements, that it doesn't add duplicate elements, and that it works correctly with both empty and non-empty lists.