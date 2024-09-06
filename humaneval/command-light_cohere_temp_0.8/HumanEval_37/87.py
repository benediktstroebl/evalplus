```python
def sort_even(lst):
    even_set = set(lst[::index::even():])
    return [::index(x) for x in lst] + [x for x in even_set if x not in [::index::even()]]

#Test cases
test_list = [1, 2, 3, 4, 6, 5, 3]
print("Result for test_list:", sort_even(test_list))  # [3, 4, 6, 5, 2, 1, 3]
test_list = [5, 6, 3, 4]
print("Result for test_list:", sort_even(test_list))  # [3, 6, 5, 4]
test_list = [1, 2, 3, 4, 5, 6]
print("Result for test_list:", sort_even(test_list))  # [3, 6, 5, 4]
```
This script defines a function sort_even that takes a list and returns a sorted list of even numbers from the original list, with the same values for even numbers. This function uses theoutines and the set to find even numbers, and then uses list comprehensions to filter out the even numbers and add them back to the original list.

The script also provides three test cases, and prints the result for each case.