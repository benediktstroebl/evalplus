```python
def sort_even(lst):
    even_list = [item for item in lst if item % 2 == 0]
    return even_list

# Test case 1
assertEqual(sort_even([1, 2, 3]), [1, 2, 3])

# Test case 2
assertEqual(sort_even([5, 6, 3, 4]), [3, 6, 5, 4])

# Test case 3
assertEqual(sort_even([10, 13, 9]), [10, 13, 9])
```
The function `sort_even` uses a list comprehension to filter out the even numbers from the input list and returns a new list containing only the even elements. This function is expected to return a list that is equal to the input list except for the odd elements, which are moved to the end of the list. The tests verify that correctness of the function by checking that the output of the `sort_even` function matches the expected output for the given input.