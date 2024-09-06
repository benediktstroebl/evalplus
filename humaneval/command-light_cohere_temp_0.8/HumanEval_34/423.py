```python
def unique(l: list):
    seen = set()
    return [x for x in l if not in seen and x not in [0, ]] 

# Test case 1: [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print("Test case 1:", unique(test_case1))  # Expected output: [0, 2, 3, 5, 9, 123]

# Test case 2: []
test_case2 = []
print("Test case 2:", unique(test_case2))  # Expected output: []

# Test case 3: ([],)
test_case3 = ([],)
print("Test case 3:", unique(test_case3))  # Expected output: []

# Test case 4: ([1, 2])
test_case4 = [1, 2]
print("Test case 4:", unique(test_case4))  # Expected output: [1, 2]

# Test case 5: ([1, 2], [3])
test_case5 = [1, 2], [3]
print("Test case 5:", unique(test_case5))  # Expected output: [1, 2] and [3]
```
This script defines a function unique that takes a list as an argument and returns a new list with unique elements from the original list. The test cases demonstrate how the