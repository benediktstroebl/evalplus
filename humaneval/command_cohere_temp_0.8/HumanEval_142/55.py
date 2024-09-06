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
This function takes as input a list of integers and squares every third element while cubing every fourth element that is not a multiple of 3. It then sums these modified elements and returns the result.

To verify the functionality, you can run the following tests:
```python
test_sum_squares_output = [(1, 2, 3), (), (-1, -5, 2, -1, -5), (0,), (10, 20, 30), (-10, -20, -30)]
for lst in test_sum_squares_output:
    assert sum_squares(lst) == 6
```
```python
test_sum_squares_output = [(), (1,), (4, 9), (8, 15, 16), (7, 21, 28, 35, 36)]
for lst in test_sum_squares_output:
    assert sum_squares(lst) == 0
```
```python
test_sum_squares_output = [(1, -5, 2, -1, -5), (-15, -5, -10, -25, -50, -100), (-4, -9, -16, -25, -36, -49, -64, -81, -100, -121, -146, -177, -200)]
for lst in test_sum_squares_output:
    assert sum_squares(lst) == -126
```
```python
test_sum_squares_output = [(10, 20, 30), (70, 140, 190), (60, 180, 240, 270, 300), (50, 150, 250, 300, 350, 400)]
for lst in test_sum_squares_output:
    assert sum_squares(lst) == 600
```
```python
test_sum_squares_output = [(-10, -20, -30), (-70, -140, -190), (-60, -180, -240, -270, -300), (-50, -150, -250, -300, -350, -400)]
for lst in test_sum_squares_output:
    assert sum_squares(lst) == -600
```
Note, that the expected output is respectively 6, 0, -126, 600 and -600 for the test cases.