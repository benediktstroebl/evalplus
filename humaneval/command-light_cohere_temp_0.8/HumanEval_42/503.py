```python
def incr_list(lst):
    return [lst[i]+1 for i, x in enumerate(lst)]

# Basic test case
print("Basic Test:", incr_list([1, 2, 3]))  # [2, 3, 4]

# Test case with lists of different lengths
print("Test with different lengths:", incr_list([5, 3, 5, 2, 3, 3] ))  # [6, 4, 6]

# Test case with negative increment
print("Test with negative increment:", incr_list([5, 3, 5, 2, 3, 3], -1)))  # [6, 4, 6]

# Test case with built-in itertools.chain_expanded_list

import itertools
lst = [5, 3, 5, 2, 3, 3]
print("Test with itertools.chain_expanded_list:", list(itertools.chain_expanded_iter(lst)))  # [6, 4, 6]

# Test case with custom increment function
def custom_incr(lst):
    return [lst[i]+1 for i, x in enumerate(lst)]
print("Test with custom increment:", incr_list(custom_incr([5, 3, 5, 2, 3, 3])))  # [6, 4, 6]
```