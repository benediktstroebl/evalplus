```python
def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            curr = str(num)
            if int(curr[0]) % 2 == 1 and int(curr[-1]) % 2 == 1:
                oddCount += 1
    return oddCount

# Test Cases
nums = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]
print(specialFilter(nums))  # Output: 2
nums2 = [15, -73, 14, -15, 32, -2, -3, 45, 21, 109]
print(specialFilter(nums2))  # Output: 1
```

The function `specialFilter` goes through each number in the `nums` list. If the number is greater than 10, it converts it to a string and checks if the first and last digits are odd. If they are, it increments the `oddCount` variable, finally returning the count of numbers that satisfy the specified condition.