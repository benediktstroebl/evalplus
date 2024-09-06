```python
def sort_even(lst):
    even_map = {x: y for y, x in enumerate(lst, 1)}
    lst = [even_map[y] for y in lst]
    return lst

# Test the function
test_lst = [5, 6, 3, 4]
test_result = sort_even(test_lst)
assert test_result == [3, 6, 5, 4]
```
This script defines a function `sort_even` that takes a list `lst` as input and returns a sorted list. The function uses a odd and even indices of the list to create a dictionary `even_map` and then uses it to transform the list to have the desired elements. The test case at the