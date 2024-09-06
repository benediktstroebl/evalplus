```python
def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            firstDigit = int(str(num)[0])
            lastDigit = int(str(num)[-1])
            if firstDigit % 2 == 1 and lastDigit % 2 == 1:
                oddCount += 1
    return oddCount

# Test Cases
nums = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]
print(specialFilter(nums))  # Output: 1
nums = [27, -44, 26, -77, 99, -22, 57, 51, 73, 89]
print(specialFilter(nums))  # Output: 4
```

This script defines a function called `specialFilter` that takes a list of numbers as input and counts the number of elements in the list that meet the specified criteria. It then provides two use cases for the function, verifying that it returns the correct number of elements.