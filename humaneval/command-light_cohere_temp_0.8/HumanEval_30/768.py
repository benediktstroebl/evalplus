```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with different lists
test_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_list2 = [-1, 2, -4, 5, 6]
test_list3 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, 10]

print(get_positive(test_list1))  # Expected Output: [2, 5, 6]
print(get_positive(test_list2))  # Expected Output: []
print(get_positive(test_list3))  # Expected Output: [5, 3, 9]
```