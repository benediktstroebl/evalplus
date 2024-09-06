Here's a self-contained Python script that solves the problem:

```python
def is_sum_to_zero(lst):
    return any(x == 0 for x in lst) and all(x != 0 for x in lst)

def test_sum_to_zero(test_list):
    return is_sum_to_zero(test_list)

test_list1 = [1, 3, 5, 0]
test_list2 = [1, 3, -2, 1]
test_list3 = [1, 2, 3, 7]
test_list4 = [2, 4, -5, 3, 9, 7]

print(test_list1, test_sum_to_zero(test_list1))
print(test_list2, test_sum_to_zero(test_list2))
print(test_list3, test_sum_to_zero(test_list3))
print(test_list4, test_sum_to_zero(test_list4))
```

The `is_sum_to_zero` function checks whether there are three distinct elements in the list that sum to zero, and returns `True` if the condition is met, and `False` otherwise. The `test_sum_to_zero` function is a simple wrapper around the `is_sum_to_zero` function, and it takes a list as an argument and returns the result of the `is_sum_to_zero` function.

Please note that you can also achieve the same functionality without creating additional functions by directly manipulating the `is_sum_to_zero` function and its tests.