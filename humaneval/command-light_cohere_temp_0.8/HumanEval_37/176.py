```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    res = [x if x % 2 == 0 else x + 1 for x in lst]
    return even_lst

def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([10, 20, 30]) == [10, 20, 30]

if __name__ == "__main__":
    test_sort_even()
```
The function `sort_even` takes a list as input and returns a new list with elements from the original list that are even numbers sorted in ascending order. The `test_sort_even` function tests the `sort_even` function with several input lists, and asserts that the output lists are correct.