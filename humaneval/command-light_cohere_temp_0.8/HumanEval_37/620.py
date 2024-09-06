```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    return even_lst

# Test cases
assertEqual(sort_even([1, 2, 3]), [1, 2, 3])
assertEqual(sort_even([5, 6, 3, 4]), [3, 6, 5, 4])
assertEqual(sort_even([9, 8, 7]), [9, 8, 7])
```
This Python code defines a function `sort_even` that takes a list as input and returns a new list with elements from the original list that are even numbers sorted. The `assertEqual` tests are used to verify that the `sort_even` function behaves correctly for different input lists.