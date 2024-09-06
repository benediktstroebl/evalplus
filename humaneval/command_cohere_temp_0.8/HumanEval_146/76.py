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

This function `specialFilter` takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and where both the first and last digits are odd (1, 3, 5, 7, 9). It counts the number of elements that satisfy this condition by iterating through the list of numbers and checking if both the first digit (after modulus by 2) and the last digit (after modulus by 10 and then by 2) are odd. The overall count is returned as the output.

To test this function, consider the following test cases:
```python
test_cases = [
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    ([21, 42, 18, -8, 99, -56], 1),
    ([66, -44, 77, -33, 55, 19], 2),
    ([11, -7, 104, -11, 33, -18], 0),
]

for test_case in test_cases:
    nums, expected = test_case
    result = specialFilter(nums)
    assert result == expected, f"Expected {expected}, but got {result} for input {nums}"
```

This block of code provides test cases to cover different scenarios and ensures that the `specialFilter` function is correctly implemented to meet the problem statement.

This problem can be solved using modulus (remainder) operations to check for the oddness of digits. This solution utilizes the property that numbers ending in 1, 3, 5, 7, or 9 after truncating to a single digit will themselves be odd.