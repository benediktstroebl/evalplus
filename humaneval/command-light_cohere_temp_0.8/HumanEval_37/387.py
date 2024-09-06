```python
def sort_even(l: list):
    """Sorts a list of numbers so that values at even indices are equal, and the function returns a new list with the sorted values."""
    l = [1, 2, 3]
    assert len(l) == 3, "List should have 3 elements"
    even = [i for i in range(len(l)) if i % 2 == 0]
    assert even == [2, 4, 6], "Even indices should have even values"
    odd = [i for i in range(len(l)) if i % 2 != 0]
    assert odd == [1, 3], "Odd indices should have odd values"
    new_list = [x for x in l if x in even] + [x for x in l if x in odd]
    assert new_list == [2, 4, 6], "Sorted even and odd values should be equal"
    return new_list
```