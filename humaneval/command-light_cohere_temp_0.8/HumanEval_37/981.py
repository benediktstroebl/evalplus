```python
def sort_even(lst):
    # Sort the list using the built-in 'sort' function with a custom key
    return sorted(lst, key=lambda x: x % 2)

# Example list to test the function
list_to_sort = [1, 2, 3, 4, 5, 6]

# Test the function
sorted_list = sort_even(list_to_sort)

# Print the sorted list
print("Sorted list:", sorted_list)

# Test again with an example list containing odd values
list_to_sort_odd = [5, 6, 3, 4]

# Test the function with the list containing odd values
sorted_list_odd = sort_even(list_to_sort_odd)

# Print the sorted list containing odd values
print("Sorted list with odd values:", sorted_list_odd)
```
The function 'sort_even' in this script employs the 'sorted' function and a custom key to sort the list. The custom key determines that values of each item in the list are divided into two categories: odd and even. The 'key=lambda x: x % 2' condition sorts the values of the list to the appropriate category. The 'sorted' list is then returned.