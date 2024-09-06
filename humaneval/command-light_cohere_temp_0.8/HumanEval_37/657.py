```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    return sorted(lst) == even_lst

# Test the function
[3, 6,5,4] should be returned
test_sort_even([3,6,5,4])
test_sort_even([5,6,3,4])
test_sort_even([1,2,3])
test_sort_even([10,20,30]) # Should return the list with even numbers sorted
```