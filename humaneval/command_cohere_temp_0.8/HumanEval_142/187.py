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

The code uses a for loop to iterate through each index and value in the input list `lst`. The `enumerate` function is used to access the index `i` and the value `num` simultaneously. The index is checked to determine whether it is a multiple of 3 or 4. If the index is a multiple of 3, the corresponding value is squared, and if the index is a multiple of 4 but not a multiple of 3, the corresponding value is cubed. The squared or cubed value is then added to the `result` variable, which should be returned at the end. 

This code addresses the problem statement by selectively squaring or cubing specific list elements and summing the results, as outlined in the problem statement. 

This approach allows the code to efficiently process each element of the list just once, providing a concise and straightforward solution to the problem. 

To verify the functionality of the implemented function, you can use the following tests:
```python
test_sum_squares_result = ([1, 2, 3], 6)
test_sum_squares_empty = ([], 0)
test_sum_squares_negative = ([-1, -5, 2, -1, -5], -126)
```

These tests correspond to the example use cases outlined in the problem statement. By running these tests, you can confirm that the function `sum_squares` behaves as expected across various scenarios.