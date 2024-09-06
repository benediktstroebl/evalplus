```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```
The function sums over the list and for each entry, squares it if the index is a multiple of 3 and cubes it if the index is a multiple of 4 and not a multiple of 3. The ensuing sum is then returned. The `**` operator is used for squaring and cubing as it is simpler and more concise than other methods. The `enumerate` command provides the index and value for each entry and allows for more readable code. 

To ensure the function handles all edge cases, update the test suite to include the following cases:
- `[1,2,3]` - This is the basic case and should return `6`. 
- `[]` - This empty list case should return `0`.
- `[-1,-5,2,-1,-5]` - This case tests both positive and negative values and should return `{-126, 0}`. 

To incorporate the test suite, add the following code:
```python
# Test Suite
lst = [1,2,3]
assert sum_squares(lst) == 6

lst = []
assert sum_squares(lst) == 0

lst = [-1, -5, 2, -1, -5]
assert sum_squares(lst) == -126
```

This script and the added test suite guarantee the function handles all edge cases and safely and accurately returns the desired sum.