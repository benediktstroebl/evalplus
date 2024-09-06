```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted."""
    return sorted(l, key=lambda x: x // 3 if x % 3 else x)

#Test cases
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
print(sort_third([10, 20, 30, 40, 50, 60, 70]))  # [10, 40, 30, 50, 60, 70]
```