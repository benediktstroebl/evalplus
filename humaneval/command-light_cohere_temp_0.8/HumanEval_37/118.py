```python
def sort_even(lst):
    # Sort the list such that all even index elements are together
    even_set = set(lst[::i for i, x in enumerate(lst) if x % 2 == 0])
    return [x for x in lst if x in even_set]

# Test cases
test_list = [5, 6, 3, 4]
test_list_sorted = sort_even(test_list)
assert test_list_sorted == [3, 6, 5, 4]

test_list = [1, 2, 3, 4, 5]
test_list_sorted = sort_even(test_list)
assert test_list_sorted == [1, 2, 3, 4, 5]

test_list = [5, 6, 3, 4, 7]
test_list_sorted = sort_even(test_list)
assert test_list_sorted == [3, 6, 5, 4, 7]

test_list = [1, 2, 3, 4, 5, 6]
test_list_sorted = sort_even(test_list)
assert test_list_sorted == [1, 2, 3, 4, 5]

```
The function takes a list `lst` as input and returns a new list `lst_sorted` where all even indices elements are sorted together. 

The function uses the set data structure to identify the even elements in the list. Then, it creates a new list that includes only the elements from `lst` that are in the set.

This script is self-contained, and it does not require any external functions or modules. It can be used as a standalone solution to the problem.