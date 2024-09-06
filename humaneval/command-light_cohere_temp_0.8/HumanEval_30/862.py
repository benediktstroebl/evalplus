```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with different lists
test_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_list2 = [-1, 2, -4, 5, 6]

print("test_list1: ", get_positive(test_list1))  # Output: [5, 3, 2, 3, 9, 123]
print("test_list2:", get_positive(test_list2))  # Output: []
``` 
This script defines a function `get_positive` that takes a list as an argument and returns a new list containing only the positive numbers from the input list. It then tests theeasy that the function on two different lists, and the results are printed.