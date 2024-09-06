```python
def specialFilter(nums):
    odd_digits = [int(i) for i in nums if i > 10 and int(str(i)[0]) % 2 == 1 and int(str(i)[-1]) % 2 == 1]
    return len(odd_digits)
```

This function uses a list comprehension to filter out numbers from the input array that meet the specified criteria - odd first and last digits and greater than 10 - and then calculates the length of this filtered list, returning it as the final result.

Here is a test suite to ensure the function correctly identifies numbers that both first and last digits are odd:
```python
def test_special_filter():
    assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([11, 19, 29, 39, 49, 59, 69, 79, 89, 99]) == 10
    assert specialFilter([2, 3, 5, 7, 9, 10, 12, 14, 15, 17, 19]) == 10
    assert specialFilter([20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 0
    assert specialFilter([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 11
    assert specialFilter([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
```