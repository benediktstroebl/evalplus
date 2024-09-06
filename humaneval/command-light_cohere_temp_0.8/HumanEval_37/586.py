```python
def sort_even(lst):
    even = [x for x in lst if x % 2 == 0]
    return even + [x for x in lst if x % 2 != 0]

# Test the function with a list of odd and even numbers
test_list = [5, 6, 3, 4]
result = sort_even(test_list)
assert len(result) == 4
assert sorted(result) == [3, 4, 5, 6]

# Test the function with a list of all numbers (odd and even)
test_all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sort_even(test_all_numbers)
assert len(result) == 10
assert sorted(result) == [1, 3, 5, 7, 9, 2, 4, 6, 8]
```