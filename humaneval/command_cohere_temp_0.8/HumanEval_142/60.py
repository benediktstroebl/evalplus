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
The code uses a for loop to iterate through each index and number in the provided list. The enumeate() function allows us to iterate through each index and value in the list. If the index is a multiple of 3, the integer value is squared. If the index is a multiple of 4 but not a multiple of 3, the integer value is cubed. The results are then added up to return the sum of all the entries. 

To ensure the functionality, here is a test suite that can be used:
```python
def test_sum_squares():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([-4, -1, -3, -2]) == -29
    assert sum_squares([-5, 10, 15, -20, 5, 6]) == 117
    assert sum_squares([]) == 0
```
You can then call the test_sum_squares() function to check if the sum_squares() function works correctly.