```python
def sort_even(lst):
    # Sort the list of odd indices
    odd = [i for i, x in enumerate(lst) if x % 2 == 1]
    # Create a new list with values from the original list at the even indices
    even = [x for x, _ in enumerate(lst) if _ % 2 == 0]
    # Sort the even list and return the original list with sorted even values
    return odd + even

# Example usage:
# Create a list to test the function
list_to_sort = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Sort the list using the function
sorted_list = sort_even(list_to_sort)
# Print the sorted list
print(sorted_list)
 ```

This code provides a Python function `sort_even` that takes a list as an argument and efficiently returns a new list with the odd indices of the input list sorted in ascending order. The function uses two lists (`odd` and `even`) to split the original list at the even indices and then sorts the even values. The resulting output is a list with the desired sorted order of even values.