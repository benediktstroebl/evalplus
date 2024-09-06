```python
def specialFilter(nums):
    oddDigits = [x for x in nums if int(x) > 10 and int(str(x)[0]) % 2 == 1 and int(str(x)[-1]) % 2 == 1]
    return len(oddDigits)
```

This function uses a list comprehension to filter out numbers from the input array that meet the specified criteria - having both first and last digits odd and being greater than 10. The condition `int(str(x)[0]) % 2 == 1 and int(str(x)[-1]) % 2 == 1` checks for odd digits at the first and last positions of the number. The length of the resulting list provides the number of elements that satisfy the condition in the input array. 

To further validate the solution, unit tests can be added to ensure it handles various cases correctly:
```python
test_cases = [
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    ([21, 43, 105, 19, 91, 5], 1),
    ([11, 3, 55, 77, 99, 333], 0),
    ([], 0),
    (['a', 'b', 'c'], 0),
]

for test in test_cases:
    assert specialFilter(test[0]) == test[1]
```

This test suite contains various test cases, including edge cases, to validate the behavior of the `specialFilter` function.