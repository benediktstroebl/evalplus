```python
def count_nums(arr):
    output = sum(int(num) for num in arr if sum(int(d) for d in str(num)) > 0)
    return output
```
This function uses a generator expression to iterate through each element in the array `arr`, converting each element to an integer `int(num)`. It then counts the number of digits in each number using a generator expression within the sum function `sum(int(d) for d in str(num))`. If the sum of the digits is greater than zero, it increments the output variable. Finally, the function returns the value of the output variable.

Here is the solution's test case:
```python
def test_count_nums():
    """
    Test the count_nums function implementation. Here are the test cases:
    >>> test_count_nums()
    """
    assert count_nums([]) == 0, "Empty array"
    assert count_nums([-1, 11, -11]) == 1, "Array with positive digit sum"
    assert count_nums([1, 1, 2]) == 3, "Array with positive digit sum"
    assert count_nums([1, -1, 2, -2, 3]) == 3, "Array with both positive and negative digits"
```