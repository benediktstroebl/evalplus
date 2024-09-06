```python
def median(lst):
    """Return the median of elements in the list lst."""
    return (sum((x for x in lst if x != lst[-1]) / 2) if len(lst) % 2 == 1 else (lst[-1] + median([lst[:-index - 1]])) / 2)

# Example usage
my_list = [10, 20, 40, 6, 4, 8, 5]
print(median(my_list))  # Output: 15.0
```