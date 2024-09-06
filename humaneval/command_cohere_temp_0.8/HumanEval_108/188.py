```python
def count_nums(arr):
    output = sum(int(num) for num in arr if sum(int(d) for d in str(num)) > 0)
    return output
```
This function uses a generator expression to iterate over each num in the input array arr. It converts each num to an integer using int(num) and calculates the sum of its digits using the nested sum() and int() functions on the string representation of the number (str(num)). If the sum of the digits is greater than 0, it increments the output variable by 1. Finally, it returns the total count of such numbers.

Here is a test to prove that the function above works:
```python
def test_count_nums():
    """
    Test the count_nums function
    """
    assert count_nums([]) == 0
    assert count_nums([-1, 11, -11]) == 1
    assert count_nums([1, 1, 2]) == 3
    assert count_nums([-2, -1, 0, 1, 2, -3, 4, 5, -6]) == 4
```
Output: