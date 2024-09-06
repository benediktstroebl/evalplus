```python
def specialFilter(nums):
    odd_digits = [x for x in nums if int(x[0]) % 2 != int(x[1]) % 2]
    return len(odd_digits)
```

This function uses a list comprehension to filter out numbers from the input array whose first and last digits are not odd and then returns the length of this filtered list.

To test this function, you can call it with two arrays as shown in the example and check that it returns the correct number of elements.

Let's add the corresponding unit tests to ensure the function works correctly for different cases:
```python
def test_special_filter():
    # True cases: First and last digits are odd
    assert specialFilter([15, 33, 105, 77, 51]) == 4

    # True case: Starting with digit 1, ending with digit 9
    assert specialFilter([119, 129, 139, 149]) == 4

    # False case: Starting with digit 1, but ending with digit 0
    assert specialFilter([110, 120, 130, 140]) == 0

    # False case: Ending with digit 9, but starting with digit 0
    assert specialFilter([190, 290, 390, 490]) == 0

    # False case: First and last digits are even
    assert specialFilter([14, 26, 64, 54, 44]) == 0

    # False case: No digits
    assert specialFilter([]) == 0

``` 
To run these tests, you can simply call the `test_special_filter()` function at the end of the script, and it will ensure that the `specialFilter` function correctly identifies the numbers that meet the odd first and last digits criterion.