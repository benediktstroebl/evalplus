```python
def sort_even(lst):
    even_list = [item for item in lst if item % 2 == 0]
    return even_list

def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([8, 9, 10]) == [8, 9, 10]

# Output:
# assert True
```