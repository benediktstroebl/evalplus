```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x+1)

#Test case:
test_even = [5, 6, 3, 4]
test_odd  = [1, 2, 3]

#Result
result_even = sort_even(test_even)
result_odd = sort_even(test_odd)

#Assertions
assert len(result_even) ==  4
assert len(result_odd) ==  3

# Assert the result of each element is correct
assert result_even[0] ==  3
assert result_even[1] ==  4
assert result_even[2] ==  5
assert result_even[3] ==  6

assert result_odd[0] ==  1
assert result_odd[1] ==  2
assert result_odd[2] ==  3
assert result_odd[3] ==  4
```
The function `sort_even` takes a list as an argument and returns a sorted list where the values of even indices are equal to the values of the corresponding even indices in the original list, but the sorting order is arbitrary.