```python
def sort_third(lst):
    """
    Function to sort list such that values divisible by three are
    retained, while other values are sorted numerically.
    """
   
    lst = list(map(lambda x: (x%3 == 0) and x <= 2, lst))
    return sorted(lst)

# Test cases
test_sort_third = []
test_sort_third.push([1, 2, 3])
test_sort_third.push([5, 6, 3, 4, 8, 9, 2])
test_sort_third.push([5, 6, 3, 4, 8, 9, 5])

# Function call and result verification
assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])
assertEqual(sort_third([5, 6, 3, 4, 8, 9, 5]), [2, 6, 3, 4, 8, 9, 5])
```
The code defines a function `sort_third` that sorts the list such that the values divisible by 3 are retained, while others are sorted numerically. The test cases contain lists of numbers, and the `assertEqual` function is used to verify the results of the function call with the expected results.