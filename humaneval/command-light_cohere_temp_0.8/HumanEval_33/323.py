```python
def sort_third(lst):
    """This function sorts a list l such that values not divisible by three remain in their original order, and the values divisible by three are sorted alphabetically.
    
    Args:
        lst (list): list of integers, potentially containing values divisible by three.
    Returns:
        list: list of integers, with values divisible by three kept in their original order and the values divisible by three sorted.
    """
Testing and usage:
>>> sort_third([1, 2, 3])
[1, 2, 3]
>>> sort_third([5, 6, 3, 4, 8, 9, 2])
[2, 6, 3, 4, 8, 9, 5]
    """

# Test cases
tests = [
    [1, 2, 3],
    [5, 6, 3, 4, 8, 9, 2],
    [3, 9, 8, 7, 6, 5, 4],
    [0, 1, 2, 3, 4, 5]
]

for test in tests:
    print(sort_third(test))
```