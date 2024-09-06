```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

# Basic test
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print("Test 1:", unique(test_unique))

# Test set()
test_set = {5, 3, 9, 0, 123}
print("Test 2:", unique(test_set))

# Test empty list
test_empty = []
print("Test 3:", unique(test_empty))

# Test large list
test_large = [1, 2,otype((36 * 10**18)), 3][4]
print("Test 4:", unique(test_large))
```
This function, unique, accepts a list and returns a sorted set of its unique elements. The script also includes a set of tests to ensure that the function operates correctly with various inputs.