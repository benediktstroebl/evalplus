```python
def count_nums(arr):
    output = sum(int(n) for n in arr if sum(int(d) for d in str(n)) > 0)
    return output
```
This function uses a generator expression to iterate over each element in the input array arr. For each element n, it calculates the sum of its digits by converting it to a string and extracting individual digits using a nested list comprehension. If the sum of the digits is greater than 0, it increments the output variable by 1. Finally, the function returns the value of output, which represents the number of elements in the array with a sum of digits greater than 0.

Here is a test suite to test this python script:
```python
def test_count_nums():
    # Empty array
    assert count_nums([]) == 0

    # Array with only positive integers
    assert count_nums([1, 5, 11, 15]) == 3

    # Array with only negative integers
    assert count_nums([-1, -5, -11, -15]) == 0

    # Array with a mix of positive and negative integers
    assert count_nums([1, -1, 11, -11, 5, -5, 15, -15]) == 2

test_count_nums()
```
The test suite includes several test cases to validate the behavior of the `count_nums` function. It checks for an empty array, an array with only positive integers, an array with only negative integers, and an array with a mix of positive and negative integers. Each test case asserts that the function's output matches the expected result.