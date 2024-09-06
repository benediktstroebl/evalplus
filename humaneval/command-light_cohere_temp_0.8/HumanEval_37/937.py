```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x - 1)

# Test case 1: Basic Test
assert sorted([1, 2, 3]) == [1, 2, 3]

# Test case 2: Lists with one element
assert sorted([1]) == [1]

# Test case 3: Lists with two elements
assert sorted([1, 2]) == [1, 2]

# Test case 4: Lists with three elements
assert sorted([1, 2, 3]) == [1, 2, 3]

# Test case 5: Lists with all even elements
assert sorted([5, 6, 3, 4]) == [4, 5, 6]
```