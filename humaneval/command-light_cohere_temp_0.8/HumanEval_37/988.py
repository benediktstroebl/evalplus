```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x + 1) % 2)

# Example usage:
# Create a list of integers
my_list = [5, 6, 3, 4, 2]

# Sort the list with even values preserved
sorted_list = sort_even(my_list)

# Print the sorted list
print(sorted_list)
```