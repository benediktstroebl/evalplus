```python
def specialFilter(nums):
    oddCounts = 0
    for num in nums:
        if num > 10:
            firstOdd = num % 2
            lastOdd = (num % 10) % 2
            if firstOdd and lastOdd:
                oddCounts += 1
    return oddCounts
```

This function `specialFilter` takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and where both the first and last digits are odd (1, 3, 5, 7, 9). It counts the number of elements that satisfy this condition by iterating through the array and checking if both the first digit (after remainder operation `%` by 2) and the last digit (after remainder operation `%` by 10 and then `%` by 2) are odd. The overall count is returned. 

The unit test for this function is also provided in the same script to ensure accuracy:
```python
test_specialFilter = lambda: assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]) == 1
```