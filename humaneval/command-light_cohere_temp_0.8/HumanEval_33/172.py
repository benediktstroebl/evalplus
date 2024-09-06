```python
def sort_third(lst):
    """Sorts a list l such that values at indices divisible by three are sorted to match the values at corresponding indices of l, but lst's other values remain as is."""
    lst[:] = sorted(lst[:], key=lambda x: x // 3 if x % 3 else x)
    return lst

# Test the function
test_list = [5, 6, 3, 4, 8, 9, 2]
test_result = sort_third(test_list)
print("Test list:", test_list)
print("Sorted list:", test_result)

# Repeat the test with different values
test_list2 = [10, 7, 9, 13, 4, 22, 21, 19]
test_result2 = sort_third(test_list2)
print("Test list:", test_list2)
print("Sorted list:", test_result2)
``` 
This script defines a function `sort_third` that takes a list as input and returns a sorted list. The function uses the the key function to sort the list such that values at indices divisible by three are sorted to match the values at corresponding indices of the original list, while the other values remain unchanged. The script then tests this function by passing a test list and printing the original list and the sorted list.