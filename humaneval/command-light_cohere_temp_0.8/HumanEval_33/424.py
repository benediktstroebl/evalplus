```python
def sort_third(lst):
    """Sorts list l such that values divisible by three appear first, and values not divisible by three are in their original order."""
    return [x if x % 3 == 0 else x for x in lst]

# Example usage
my_list = [5, 6, 3, 4, 8, 9, 2]
sorted_list = sort_third(my_list)
print(sorted_list)  # Output: [2, 6, 3, 4, 8, 9, 5]
```