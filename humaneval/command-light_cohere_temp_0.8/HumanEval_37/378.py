```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    return even_lst

even_lst = sort_even([1, 2, 3])
assert even_lst == [1, 2, 3]

even_lst = sort_even([5, 6, 3, 4])
assert even_lst == [3, 6, 5, 4]

even_lst = sort_even([9, 8, 7])
assert even_lst == [7, 8, 9]

def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([7, 8, 9]) == [7, 8, 9]

if __name__ == "__main__":
    test_sort_even()
```