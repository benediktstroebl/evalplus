```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    return even_lst

# Test cases
assert sort_even([1, 2, 3]) == [1, 2, 3]
assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
``` 
The function takes a list lst and returns a new list, even_lst, which is the list of elements from lst that are even numbers. The function then returns even_lst.