```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    def check(test_list):
        return all(x % 3 == i for i, x in enumerate(test_list))

    return sorted(l, key=lambda x: (check(list(x)), x))

# Example usage
my_list = [1, 2, 3, 9, 5, 6, 8, 4]
print(sort_third(my_list))
```