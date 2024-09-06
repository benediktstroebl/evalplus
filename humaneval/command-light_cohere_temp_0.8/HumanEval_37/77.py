```python
def sort_even(lst):
    even_set = set(lst[::int((i+1) % 2) :: 2:: int()) for i in range(len(lst)))
    return [int(e) for e in even_set]

# Test cases
test_list = [5, 6, 3, 4]
test_list_sorted = sort_even(test_list)
assert test_list_sorted == [3, 6, 5, 4]

test_list_with_odd = [1, 2, 3]
test_list_sorted_with_odd = sort_even(test_list_with_odd)
assert test_list_sorted_with_odd == [1, 2, 3]

test_list_empty = []
test_list_sorted_empty = sort_even(test_list_empty)
assert test_list_sorted_empty == []
```
The function `sort_even` receives a list and returns a sorted list with even items. The test cases use a passing a variety of test scenarios. 

The test cases assert that the sorted lists produced by the function match the expected results.