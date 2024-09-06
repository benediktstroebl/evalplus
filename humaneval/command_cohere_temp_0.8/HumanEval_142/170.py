```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

The code uses a for loop to iterate through each index `i` and corresponding value `num` in the input list `lst`. The condition `i % 3 == 0` checks if the index is a multiple of 3, in which case it squares the corresponding number. Alternatively, the condition `i % 4 == 0 and i % 3 != 0` checks if the index is both a multiple of 4 and not a multiple of 3, in which case it applies the cubic function to the corresponding number. All other entries are left unchanged, and the sum of the modified (squared or cubed) numbers is returned. 

To ensure correctness, it is essential to carefully consider and enumerate the various conditional checks present in the problem statement. 

This script solves the function described in the problem statement and will return the sum of all modified entries in the list. 

To test this script, make sure to provide the input lists with varying numbers and indices to ensure the function behaves correctly for different scenarios.