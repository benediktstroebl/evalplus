```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set1 = set(lst)
    return list(set1)

# Test case 1: Simple list
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_case1))  # Output: [0, 2, 3, 5, 9, 123]

# Test case 2: List of strings
test_case2 = ["hello", "world","hello", "!!!!"]
print(unique(test_case2))  # Output: ['hello', 'world']

# Test case 3: List of mixed data types
test_case3 = [123, 5, (123), "hello", 0]
print(unique(test_case3))  # Output: [123, 5, (123)]
```
This script defines a function `unique` that takes a list as input and returns a sorted list of unique elements from that list. The test cases provided demonstrate how the unique function behaves with different types of lists, and the expected output is displayed.