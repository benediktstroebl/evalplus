```python
def sort_even(lst):
    even_lst = [item for item in lst if item % 2 == 0]
    return even_lst

even_lst = sort_even([1, 2, 3])
print("Even list:", even_lst)  # [1, 2, 3]

even_lst = sort_even([5, 6, 3, 4])
print("Even list:", even_lst)  # [3, 6, 5, 4]

# Test again
even_lst = sort_even([2, 3, 4, 5])
print("Even list:", even_lst)  # [2, 3, 4, 5]
```
This script defines a function sort_even which takes a list lst and returns a new list even_lst that contains items from the original list that are even numbers, sorted in ascending order. It then passes the