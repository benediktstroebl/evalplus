```python
def sort_even(lst):
    return sorted([x for x in lst if x % 2 == 0], key=lambda x: x)

# Test case: sort even function with a list containing odd and even numbers
test_even = [1, 2, 3]
result = sort_even(test_even)
assert [x for x in result if x % 2 == 0] == [1, 2, 3]

# Test case 2: sort even function with list containing only even numbers
test_only_even = [4, 6, 8, 10]
result_second = sort_even(test_only_even)
assert result_second == [4, 6, 8, 10]
```
This Python script defines a function called `sort_even` that sorts a list of numbers based on whether they are even or odd. The function uses a simple filtering to identify even numbers and then sorts them separately from odd numbers. The test cases demonstrate the both scenarios of using the `sort_even` function, passing lists containing numbers with both odd and even numbers, and a list containing only even numbers, respectively. The script then checks if the results of the function are as expected.