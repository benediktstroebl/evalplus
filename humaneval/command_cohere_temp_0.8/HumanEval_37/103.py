```python
def sort_even(l):
    even = l[::2]
    odd = l[1::2]
    return even + sorted(odd)
```

The script uses list comprehension to divide the list into two parts - odd and even indices. The odd indices are left as they are, while the even indices are sorted and then returned together with the odd indices. This way, the original list is returned with the even indices sorted. 

Here is a test case that can be used to verify the functionality of the provided code:
```python
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([7, 22, 14, 27, 31, 8, 23]) == [8, 14, 22, 23, 27, 31, 7]
```