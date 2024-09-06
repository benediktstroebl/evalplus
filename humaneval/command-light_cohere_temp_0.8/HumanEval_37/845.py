```python
def sort_even(lst):
    return lst[:]  # return list with all even indices

# Test cases 1
test_1 = [1, 2, 3]
test_1_result = sort_even(test_1)
assert test_1_result == [2, 3, 1]

# Test cases 2
test_2 = [5, 6, 3, 4]
test_2_result = sort_even(test_2)
assert test_2_result == [3, 6, 5, 4]

# Test cases 3
test_3 = [2, 3, 4, 5, 6]
test_3_result = sort_even(test_3)
assert test_3_result == [2, 4, 6, 3, 5]

# Test cases 4
test_4 = [1, 5, 6]
test_4_result = sort_even(test_4)
assert test_4_result == [5, 6, 1, 4]

print("All tests passed!")
```