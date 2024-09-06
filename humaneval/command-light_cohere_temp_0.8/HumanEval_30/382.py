```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with different lists

# Lists with all numbers, positive and negative
test_list1 = [1, 2, 3, 4, 5, -1, 6]
test_list2 = [-2, 3, -100, 4, -5, 6, 7]
test_list3 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

# Check if the function correctly returns only positive numbers
assert get_positive(test_list1) == [1, 2, 3, 4, 5, 6]
assert get_positive(test_list2) == [-2, 3, 4, 6, 7]
assert get_positive(test_list3) == [5, 3, 2, 3, 9, 123]
 ```