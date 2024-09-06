```python
def sort_even(l: list):
    """Sorts list l of integers into ascending order of even values."""
    l = [x for x in l if x % 2 == 0]
    return sorted(l)

# Test the function with some example lists
test_list = [5, 6, 3, 4, 1]
result = sort_even(test_list)
assert [3, 6, 5, 4, 1] == result

test_list2 = [7, 2, 8, 5, 4]
result2 = sort_even(test_list2)
assert [8, 5, 4, 7, 2] == result2
```
The function `sort_even` in this code takes a list of integers as input and returns a sorted list of even numbers. The list comprehension is used to filter out the odd numbers first, then the sorted function is applied to the remaining even numbers. The resulting sorted list is then compared with the expected results using assertions.