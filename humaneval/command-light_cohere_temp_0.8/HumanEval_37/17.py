```python
def sort_even(lst):
    return lst[:] if len(lst) % 2 == 0 else lst[:len // 2] + lst[-len // 2:]

# Test case 1:
# Function should return the original list when input is an odd number of elements
test_case1 = [5, 6, 3, 4]
assert sort_even(test_case1) == test_case1

# Test case 2:
# Function should return the list with even number of elements
test_case2 = [3, 6, 5, 4]
assert sort_even(test_case2) == [3, 6, 5, 4]

# Test case 3:
# Function should return a sublist with an even number of elements
test_case3 = [1, 2, 3, 4, 5, 6]
assert sort_even(test_case3) == [2, 3, 4]
```