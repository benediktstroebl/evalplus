```python
def sort_even(lst):
    # Create a new list to hold the sorted elements with even indices
    lst_even = [x for x in lst if x % 2 == 0]
    
    # Sort the new list
    lst_even.sort_even = sorted(lst_even)
    
    # Return the sorted list
    return lst_even

# Example usage

# Test list with odd and even indices
list_data = [5, 6, 3, 4, 2, 1]

# Call the sort_even function
sorted_data = sort_even(list_data)

# Print the sorted list
print(sorted_data)
```
This code defines the function `sort_even`, which sorts a list so that the elements with even indices are in the same relative order. The example usage demonstrates how to use this function with a test list and prints the sorted list.