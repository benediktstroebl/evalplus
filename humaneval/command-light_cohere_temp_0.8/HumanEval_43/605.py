```python
def pairs_sum_to_zero(l):
    """
    Function that checks whether all pairs of elements in the list sum to zero.
    """
    def check_sum(x, y):
        return x + y == 0
    return all(check_sum(x, y) for x, y in zip(l, l[1:]))

# Example usage
test_list = [1, 3, 5, 0]
result = pairs_sum_to_zero(test_list)

if result:
    print("All pairs sum to zero!")
else:
    print("No valid combination found.")
```
This script defines a function called `pairs_sum_to_zero` that checks whether there is a combination of elements in a list where all pairs add up to zero. The `check_sum` helper function returns `True` if the sum of the two elements is zero, and `False` otherwise. The `all` function with generator expression is then used to check that this holds for all pairs of distinct elements in the list. 

The script provides an example list and runs the `pairs_sum_to_zero` function on it. If the result is `True`, the script prints "All pairs sum to zero!". Otherwise, the script prints "No valid combination found."