```python
def sort_even(lst):
    even_lst = []
    for x in lst:
        if x % 2 == 0:
            even_lst.append(x_val(x))
    return even_lst

# Test 1
test_lst = [1, 2, 3]
even_lst = sort_even(test_lst)
assert even_lst == [1, 2, 3]

# Test 2
test_lst = [5, 6, 3, 4]
even_lst = sort_even(test_lst)
assert even_lst == [3, 6, 5, 4]

# Test 3
test_lst = [10, 9, 8, 7]
even_lst = sort_even(test_lst)
assert even_lst == [7, 8, 9, 10]

# Test 4
test_lst = [0, 1, 2, 3]
even_lst = sort_even(test_lst)
assert even_lst == [0, 1, 2, 3]

# Test 5
test_lst = [5, 6, 7, 8, 9]
even_lst = sort_even(test_lst)
assert even_lst == [8, 9, 6, 7]

# Test 6
test_lst = [0, 9, 8, 7]
even_lst = sort_even(test_lst)
assert even_lst == [0, 8, 7, 9]
```

This Python code provides a function named `sort_even` designed to sort a list of numbers into a subset where the values at even indices are equal, while keeping the original relative order of the odd values. The function achieves this desired output by iterating through the input list and categorizing values based on their parity. The script then tests the test the function with various input lists, verifying that the output matches the expected result.