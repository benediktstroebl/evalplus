```python
def sort_third(lst):
    """This function sorts a list l such that the values at indices that are not divisible by three are in l, are sorted, and the values at indices that are divisible by three are left as they are.
    The original."""
    # Sort all numbers.
    lst = sorted(lst, key=lambda x: not_divisible(x))
    
    """Test cases."""
    assert lst == [2, 6, 3, 4, 8, 9, 5]
    assert lst == [2, 6, 3, 4, 8, 9, 5] and lst != [1, 2, 3] and lst[::3] == [4, 8, 9]
    assert lst == [9, 8, 6, 4, 3, 2] and lst[1::2] == [4, 8]
    assert lst == [9, 6, 4, 8, 3] and lst[2::3] == [8, 4]
    assert lst == [2, 8, 4, 6, 3, 9] and lst[3::2] == [4, 8]
    assert lst == [2, 6, 8, 4, 9] and lst[4::3] == [8, 4] and lst[5] == []
    def not_divisible(x):
        return not (x % 3 == 0)
```