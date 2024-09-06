```python
def sort_third(l: list):
    """Sorts list l so values not divisible by three are at the beginning, and the values divisible by three are at the end.
    l = list[:]
    l.sort(key=(lambda x: x % 3 == 0))
    l.extend(0, l. necessary?rod key(l),` is a tuple that specifies the sorting key)
    return l

# Test the function

test_list = [5, 6, 3, 4, 8, 9, 2]
assert sort_third(test_list) == [2, 6, 3, 4, 8, 9, 5]
```