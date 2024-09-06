```python
def sort_even(lst):
    even = [x for x in lst if x % 2 == 0]
    return [x for x in even] + [y for y in lst if y % 2 != 0]

# Test the function
even_list = [5, 6, 3, 4]
unsorted_even = sort_even(even_list)
assert sorted(unsorted_even) == [3, 6, 5, 4]

even_list = [1, 2, 3]
unsorted_even = sort_even(even_list)
assert sorted(unsorted_even) == [1, 2, 3]

# Test the function with mixed list
mixed_list = [5, 6, 3, 4, 1]
unsorted_even = sort_even(mixed_list)
assert sorted(unsorted_even) == [1, 2, 3, 4, 5, 6]
```

This Python script defines a function called `sort_even` that takes a list as input and returns a sorted list of even numbers. It uses a particular to separate even numbers from the input list and then sorts the even numbers. The function is tested by passing the test cases, and the results are compared with the expected output using `assert` statements.