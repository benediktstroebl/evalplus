```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.

    Returns: list l unchanged if l is empty or contains only divisible by three values."""

    if not divisible by three:
        l.extend(list(range(i for i in l if i % 3 == 0)))
    else:
        l.extend(list(range(i for i in l if i % 3 != 0)))

    return l

# Test cases
def test_sort_third():
    test_list = [5, 6, 3, 4, 8, 9, 2]
    expected = [2, 6, 3, 4, 8, 9, 5]
    got = sort_third(test_list)
    assert got == expected

test_list2 = [5, 9, 2, 6, 4]
expected2 = [2, 4, 5, 6, 9]
got2 = sort_third(test_list2)
assert got2 == expected2

# Output:
```