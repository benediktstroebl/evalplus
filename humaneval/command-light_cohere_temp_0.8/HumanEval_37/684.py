```python
def sort_even(lst):
    even_list = [x for x in lst if x % 2 == 0]
    return even_list

# Test the function with several inputs
assertEqual(sort_even([1, 2, 3]), [1, 2, 3])
assertEqual(sort_even([5, 6, 3, 4]), [3, 6, 5, 4])
assertEqual(sort_even([11, 22, 33, 44]), [11, 22, 33, 44])
assertEqual(sort_even([9, 10, 91, 100]), [91, 100, 9, 10])
```
This code defines a function **`sort_even`** that takes a list and returns a new list with the elements from the original list that are even indices. The function uses a list comprehension to filter even numbers from the original list and then returns the new list. The code also provides several test cases to verify the correctness of the **`sort_even`** function.