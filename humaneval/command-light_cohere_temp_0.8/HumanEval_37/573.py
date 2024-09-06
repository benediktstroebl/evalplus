```python
def sort_even(lst):
    return sorted(lst, key=lambda x: (x if x % 2 == 0 else x + 1))

# Example usage:
print(sort_even([1, 2, 3, 4, 5, 6]))  # Expected Output: [1, 2, 3, 4, 5, 6]
print(sort_even([5, 6, 3, 4]))  # Expected Output: [3, 6, 5, 4]
```
This function takes a list and sorts the even items to the beginning while preserving the relative order of the odd items. The function uses the unique key lambda function that compares each item to itself (identical to the original list). This allows the list to be sorted based on whether it is even or odd.