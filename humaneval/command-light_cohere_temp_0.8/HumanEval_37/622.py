```python
def sort_even(lst):
    even_list = [x for x in lst if x % 2 == 0]
    return even_list if even_list is not None else [even_list] + lst[1:]

# Unit tests
test_sort_even = [
    'def test_odd(): assert sort_even([1, 2, 3]) == [1, 2, 3]
    'def test_even(): assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]'
]
``` 
This code defines a function, `sort_even`, that sorts a list so that the even numbers are at the front, and the odd numbers are at the back. It uses a time list of numbers to be elements of the list, which will pass through the function.