```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted."""
    return [3 for _ in range(3) if i % 3 != 0 else [i] for i in l] + [i for i in l if i % 3 != 0]

#Test cases
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
print(sort_third([10, 15, 20]))  # [20, 15, 10]
print(sort_third([27, 54, 117]))  # [27, 117, 54]
```