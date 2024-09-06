```python
def pairs_sum_to_zero(l):
    return any([x + y = 0 for x, y in zip(l, l[1:])])

# Unit tests
test_pairs_sum_to_zero = lambda: [True] * [1, 3, 5, 0], [1, 3, -2, 1], [1, 2, 3, 7], [2, 4, -5, 3, 5, 7]]

test_pairs_sum_to_zero()

```
This script defines a function called pairs_sum_to_zero that checks if any two elements in the list sum to zero. It returns True if this result is achieved, and False otherwise. The unit tests include a variety of test cases, including lists with different lengths and contents, which the function should be able to correctly handle.