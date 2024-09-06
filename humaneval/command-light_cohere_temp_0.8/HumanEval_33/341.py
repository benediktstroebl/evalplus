```python
def sort_third(lst):
    """This function sorts a list l such that all items not divisible by three are at the beginning."""
    # [0, 2, 3] is the only segment not divisible by 3
    return lst[:3] + lst[3::3]

# Test cases
print(sort_third([1, 2, 3]))  # Expected Output: [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # Expected Output: [2, 6, 3, 4, 8, 9, 5]
print(sort_third([10, 25, 50, 12, 30]))  # Expected Output: [10, 12, 30, 25, 50]
```