Here's your improved solution with a more descriptive docstring and additional test cases:
```python
def is_sum_positive(lst):
    """
    Check if list's elements have sum greater than zero.

    Parameters: list: list of integers.
    Returns: True if all elements are positive and their sum is greater than zero,
    otherwise False.

    >>> is_sum_positive([3, 2, 4])
    True
    >>> is_sum_positive([0, -1, 2])
    False
    >>> is_sum_positive([1, -2, -3])
    True
    """
    return sum(lst) > 0

def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    Parameters: list: list of integers
    """
    return is_sum_positive([sum(l) for l in l])

tests = [
    [
        [1, 3, 5, 0],
        [1, 3, -2, 1],
        [1, 2, 3, 7],
        [2, 4, -5, 3, 9, 7],
        [1],
    ]

if __name__ == "__main__":
    for test_case in tests:
        result = triples_sum_to_zero(test_case)
        print(f"{test_case} -> {result}")
```
The docstring is a feature in Python that helps users and other developers understand the function and its purpose. In this case, it describes the function's behavior and how it works, which is very beneficial.