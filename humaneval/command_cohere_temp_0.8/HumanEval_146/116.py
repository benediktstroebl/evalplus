```python
def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            currentDigits = [int(digit) for digit in str(num)]
            if currentDigits[0] % 2 == 1 and currentDigits[-1] % 2 == 1:
                oddCount += 1
    return oddCount

# Tests
nums = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]
test_cases = [([case], expected) for (case, expected) in zip(nums, [1, 0, 0, 1, 2])]

for nums, expected in test_cases:
    assert specialFilter(nums) == expected
```
This script defines the `specialFilter` function, which takes an array of numbers as input and counts the number of elements in the array that meet the specified criteria (both first and last digits are odd). It then uses assert statements to check the result for each input against the expected output from the problem statement.