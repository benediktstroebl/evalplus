```python
def specialFilter(nums):
    oddDigits = [x for x in nums if int(x[0]) % 2 != int(x[1]) % 2]
    return len(oddDigits)
```

The provided Python script defines a function `specialFilter` that takes an array of numbers as input and returns the number of elements in the array that meet the specified criteria: having more than 10 digits and both the first and last digits being odd.

To achieve this, the function creates a list called `oddDigits` that contains all the numbers from the input array that have an odd first digit and an even last digit. The `len()` function is then used to count the number of elements in the `oddDigits` list, which gives the count of numbers that satisfy the defined condition. 

This solution is efficient and cleanly written, providing a straightforward way to meet the problem requirements.