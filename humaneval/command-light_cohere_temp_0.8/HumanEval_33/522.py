```python
def sort_third(lst):
    """This function sorts a list l such that all the numbers not divisible by three are at the beginning, and the numbers divisible by three are at the end.
    return sorted(lst)[::3] if lst else []
    """
    assert sorted(lst)[::3:] == [2, 6, 3, 4, 8, 9, 5]
    assert sorted(lst)[2::3] == [8, 9, 5]
    assert sorted(lst)[0::3] == [6, 3, 4]
    assert sorted(lst)[1::3] == [2, 8, 9]
    return sorted(lst)

# Example usage
my_list = [5, 6, 3, 4, 8, 9, 2]
print(sort_third(my_list))
```