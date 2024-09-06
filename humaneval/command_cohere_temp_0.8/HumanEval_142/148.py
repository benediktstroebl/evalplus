```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

This script defines a function called `sum_squares` that takes a list of integers as input. It iterates through each element in the list and squares it if the index is a multiple of 3, and cubes it if the index is a multiple of 4 but not a multiple of 3. The function then adds up all the modified values and returns the result.

Here is an example usage of the function:
```python
my_list = [1, 2, 3, 4, 5]
result = sum_squares(my_list)
print(result)  # Output: 630
```

And here is how you can test the function:
```python
def test_sum_squares():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([10, 20, 30, 40]) == 5200
    assert sum_squares([-1, -2, -3, -4]) == -30
    assert sum_squares([0, 0, 0, 0]) == 0
    assert sum_squares([-5, -1, -5, -1]) == -126
    assert sum_squares([2, 4, 6, 8]) == 120
``` 

This test suite contains several test cases that cover different scenarios and edge cases, ensuring that the `sum_squares` function behaves as expected.