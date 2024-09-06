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

The code uses a for loop to iterate through each index and value in the input list `lst`. By using the `enumerate` function, the loop simultaneously provides the index `i` and the value `num` for each entry in the list. 

For each entry, the code checks whether the index is a multiple of 3 using the modulo operator `%`. If the index is a multiple of 3, the value is squared using the power operator `**`. If the index is a multiple of 4 and not a multiple of 3 (i.e., mutually exclusive), then the power operator is set to 3 to cube the integer value. The results are accumulated in the variable `result` and returned upon completion.

This algorithm optimizes the computation by utilizing the index iterator to modify the numeric values accordingly, ultimately providing a concise solution. 

The unit tests for this code can be used to verify its correctness. Given the example test cases provided in the problem, the unit tests can be structured as follows:
```python
def test_sum_squares():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([-1, -5, 2, -1, -5]) == -126
    assert sum_squares([0, 0, 0, 0, 0]) == 0
    assert sum_squares([7, 8, 9, 10, 11]) == 298
```