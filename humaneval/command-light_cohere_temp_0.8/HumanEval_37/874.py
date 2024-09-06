```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    return even_lst

def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
``` 
This Python function, sort_even, takes a list as input and creates a new list, even_lst, that only includes the elements from the original list that are even numbers. It then returns this same_list, which contains the elements from the original list in the same order as the even numbers.