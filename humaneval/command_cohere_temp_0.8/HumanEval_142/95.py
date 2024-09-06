```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num = num**2
        if i % 4 == 0 and i % 3 != 0:
            num = num**3
        result += num
    return result
```
This function employs a for loop to iterate through each entry in the input list. It utilizes the modulo operator to check the index of each entry, squared for indexes that are multiples of three and cubed for indexes that are multiples of four but not multiples of three. The sum is then returned by the function. 

Here is a test suite that can be used to validate the functionality of this problem:
```python
def test_sum_squares():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([-1, -5, 2, -1, -5]) == -126
    assert sum_squares([0, 0, 0, 0, 0]) == 0
    assert sum_squares([10, 20, 30, 40, 50]) == 2550
```
To test the function, three unit tests are defined, each verifying the function's behavior for a specific input list, ensuring that the expected output matches the output of the function. 
The tests can be executed by running `test_sum_squares()`, and the assertions will verify that the function behaves as expected.