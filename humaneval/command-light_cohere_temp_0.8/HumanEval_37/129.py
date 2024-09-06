```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    odd_lst = [y for y in lst if y % 2 != 0]
    return even_lst

# Test cases
test_1 = [1, 2, 3]
test_2 = [5, 6, 3, 4]
test_3 = [10, 20, 30, 40]

# Function call and results
test_1_result = sort_even(test_1)
test_2_result = sort_even(test_2)
test_3_result = sort_even(test_3)

assert test_1_result == [1, 2, 3]
assert test_2_result == [3, 6, 5, 4]
assert test_3_result == [30, 20, 10, 40]
```
This script defines a function `sort_even` which takes a list `lst` as input and returns a new list `even_lst` that has elements from `lst` that are even numbers. It then creates two lists: `odd_lst` with elements that are not even numbers, and `even_lst` with elements that are even numbers. The function then returns `even_lst`, which will be equal to `lst` in terms of even numbers, but sorted. 

The test cases are defined at the end, with the `test_1` list having elements 1, 2, and 3, and `test_2` list having elements 5, 6, 3, and 4. The `sort_even` function is then called with these lists, and the results are stored in `test_1_result` and `test_2_result`. Finally, the test cases are asserted to check that the results are equal to the expected values.