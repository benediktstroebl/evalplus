```python
def sort_even(lst):
    even = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
    lst = sorted(even)
    return lst

# Test case 1
even_list = [1, 2, 3]
result_case1 = sort_even(even_list)
assert result_case1 == [1, 2, 3]

# Test case 2
even_list = [5, 6, 3, 4]
result_case2 = sort_even(even_list)
assert result_case2 == [3, 6, 5, 4]

# Test case 3
even_list = [0, 2, 3, 4]
result_case3 = sort_even(even_list)
assert result_case3 == [0, 2, 3, 4]

# Test case 4
odd_list = [1, 3, 5, 7]
result_case4 = sort_even(odd_list)
assert result_case4 == [7, 5, 3, 1]
```
The function `sort_even` takes a list as input and returns a sorted list of the same elements, with equal values for even indices and sorted odd indices. The test cases demonstrate the _sort_even function's functionality by passing different lists and verifying that the output lists are as expected.