```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```

The code uses a for loop to iterate through each index `i` and corresponding list `num` in `lst`. The modulus operations are used to determine whether the index is a multiple of 3 or 4. If the index is a multiple of 3, the corresponding `num` is squared, and if the index is a multiple of 4 and not a multiple of 3, the corresponding `num` is cubed. The sum is then returned after iterating through the list.

The unit tests are correctly integrated through the `test_sum_squares` function, which verifies that the function outputs correct results for the example use cases provided in the problem statement. 

```python
def test_sum_squares():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126
```

You can run this test file by adding the test case assertions and running the script with the command `python test_sum_squares.py` in your terminal. 

This approach will successfully pass the provided tests and solve the problem in a self-contained manner, as required.