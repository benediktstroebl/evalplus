```python
def specialFilter(nums):
    oddCounts = 0
    for num in nums:
        if num > 10:
            firstDigit = int(str(num)[0])
            lastDigit = int(str(num)[-1])
            if firstDigit % 2 == 1 and lastDigit % 2 == 1:
                oddCounts += 1
    return oddCounts
```

The function `specialFilter` uses a loop to iterate through each number in the input `nums` array. For each number, it checks if the number is greater than 10. If so, it calculates the first and last digits of the number by indexing the string representation of the number and calculates the remainder of the first digit and the last digit when divided by 2. If both remainders are 1, it increments the `oddCounts` variable by 1. Finally, the function returns the value of `oddCounts`.

Here's a test case to test the above function:
```python
test_cases = [
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    ([21, 109, 543, 557, 821, 19, 99], 3)
]

for expected, nums in test_cases:
    actual = specialFilter(nums)
    assert actual == expected, f"Failed with {actual} vs {expected}"
```

This test case includes a variety of arrays with different numbers, and the expected output is provided for each array. The function is tested against these different inputs to ensure it produces the expected result for each test case.