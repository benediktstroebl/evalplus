```python
def sort_even(lst):
    # Sort even numbers from index 0
    even_start = len(lst) // 2
    even_end = even_start + 1
    return lst[:even_start] + [x for x in lst[even_start:even_end] ] + lst[even_end:]

# Test the function with various lists
test_lists = [ [ [1, 2, 3], [5, 6, 3, 4], [5, 6, 7, 2, 8, 3], [1, 2, 3, 4, 5, 6]]
for test_list in test_lists:
    actual_list = sort_even(test_list)
    print("List after sorting:", actual_list)
```
The function `sort_even` sorts a list of numbers into the first half of the list contains even numbers and the second half contains numbers that are odd. The output of the `sort_even` is identical to the original list, except the odd numbers have been moved to the end of the list.