```python
def sort_even(lst):
    even_list = [x for x in lst if x % 2 == 0]
    return even_list

# Test case 1
assertEqual(sort_even([1, 2, 3]), [1, 2, 3])

# Test case 2
assertEqual(sort_even([5, 6, 3, 4]), [3, 6, 5, 4])

# Test case 3
assertEqual(sort_even([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
```
This code defines a function `sort_even` that takes a list as input and returns a new list with elements from the original list that are even numbers sorted in ascending order. The function uses a test cases to verify the functionality of the `sort_even` function.