```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    Args:
    l (list): list to be sorted
    Returns:
    l' (list): list of integers, where values at indices that are divisible by 3 are identical, and the
    remaining values are sorted.
    """
    function returns nothing."""

# Example 1
l = [1, 2, 3]
print("Example 1 output:", end="flush")
l = sort_third(l)
print(" -> ", end="flush)
print(*l)

# Example 2
l = [5, 6, 3, 4, 8, 9, 2]
print("Example 2 output:", end="flush")
l = sort_third(l)
print(" -> ", end="flush)
print(*l)

# Example 3
l = [10, 9, 8, 7, 6, 5, 3, 2]
print("Example 3 output:", end="flush")
l = sort_third(l)
print(" -> ", end="flush)
print(*l)
```