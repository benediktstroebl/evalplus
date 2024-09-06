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

The code uses a for loop to iterate through each index and value in the input list `lst`. The `enumerate` function is used to access the index `i` and the value `num` simultaneously. The index is then checked to see if it is a multiple of 3 or 4 using the modulo operator `%`. If the index is a multiple of 3, the value is squared (`**= 2`) before its square is added to the `result`. If the index is not a multiple of 3 but is a multiple of 4, the value is cubed (`**= 3`) before its cube is added to the `result`. Finally, the sum of the squares (or cubes) is returned.

This Python script solves the problem using a single, self-contained function `sum_squares` with no external dependencies, resulting in a clean and efficient solution.