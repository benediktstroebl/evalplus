```python
def incr_list(lst):
    new_lst = []
    for num in lst: 
        new_lst.append(num + 1)
    return new_lst

# Test the function
test_incr_list = []
test_incr_list.append([1, 2, 3])
test_incr_list.append([5, 3, 5])
test_incr_list.append([5, 3, 5])
test_incr_list.append([6, 3, 5])
test_incr_list.append([5, 3, 5])
test_incr_list.append([5, 3, 5])
test_incr_list.append([5, 3, 5])
test_incr_list.append([6, 3, 5])
test_incr_list.append([7, 0])

# Call the function with the test input and assert the output matches the expected output
assert incr_list(test_incr_list) == [6, 4, 6, 3, 4, 4, 6, 4, 10, 1, 124]
```