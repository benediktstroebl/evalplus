```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float('inf')]

# Test case 1: Unique elements from a list
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print("Test case 1:", unique(test_case1))  # Expected output: [0, 2, 3, 5, 9, 123]

# Test case 2: Unique elements from a list of strings
test_case2 = ["hello", "world", "!"]
print("Test case 2:", unique(test_case2))  # Expected output: ['hello', 'world', '!!']

# Test case 3: Unique elements from a list containing float('inf')
test_case3 = [5, float('inf'), 3]
print("Test case 3:", unique(test_case3))  # Expected output: [5, float('inf')]
```
The function `unique` takes a list `lst` as input and returns a new list containing only the unique elements from the original list. It uses a other set data structure to keep track of the unique elements and returns the resulting unique list.