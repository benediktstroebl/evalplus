```python
def count_nums(arr):
    output = sum(int(num) for num in arr if sum(int(d) for d in str(num)) > 0)
    return output
```
This function uses a generator expression to iterate over each num in the input array arr. It converts each num to an integer using int(num) and calculates the sum of its digits using the nested generator expression sum(int(d) for d in str(num)). If the sum of the digits is greater than 0, it contributes to the total sum. Finally, the function returns the total count of numbers with positive digit sums.

Here is a test suite to verify its correctness:
```python
def test_count_nums():
    # Basic Test Cases
    assert count_nums([]) == 0
    assert count_nums([-1, 11, -11]) == 1
    assert count_nums([1, 1, 2]) == 3

    # Test Case with Negative Numbers
    assert count_nums([−123, −13, −14, 321]) == 2

    # Test Case with Positive Numbers
    assert count_nums([7, −3, 14, 15, −1, 0, 5, 6]) == 6

    # Test Case with Mixed Numbers
    assert count_nums([−1, 2, 3, −4, 5, 10, −2, 7, −3]) == 8

    # Test Case with Large Input
    large_input = [i for i in range(1000, 10000)]
    large_input.append(12)
    assert count_nums(large_input) == 10

    # Edge Case: Single Element
    assert count_nums([-123]) == 1

test_count_nums()
```
This test suite includes several test cases to validate the behavior of the count_nums function with both positive and negative integers and various input sizes.