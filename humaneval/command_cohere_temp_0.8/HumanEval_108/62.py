```python
def count_nums(arr):
    output = sum(int(num) for num in arr if sum(int(d) for d in str(num)) > 0)
    return output
```
This function uses a generator expression to iterate over each element in the input array arr. It converts each element to an integer using int(num) and checks if the sum of its digits is greater than 0. If the condition is met, the element is included in the sum, and the total count is returned as the output of the function.

Here is a test suite to verify the correct functionality of the solution:
```python
def test_count_nums():
    # Empty array
    assert count_nums([]) == 0

    # Array with only positive integers
    assert count_nums([1, 5, 11, 15]) == 3

    # Array with only negative integers
    assert count_nums([-1, -5, -11, -15]) == 0

    # Mixed array of positive and negative integers
    assert count_nums([1, -1, 11, -11, 2, -2, 3, -3]) == 3

test_count_nums()
```
The test suite contains three assertions that test the function with different scenarios: an empty array, an array with only positive integers, an array with only negative integers, and a mixed array of positive and negative integers. The tests verify that the function returns the expected count of elements that have a sum of digits greater than 0.