```python
def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            currentDigit = int(str(num)[0])
            lastDigit = int(str(num)[-1])
            if currentDigit % 2 == 1 and lastDigit % 2 == 1:
                oddCount += 1
    return oddCount

# Test Cases
nums1 = [15, -73, 14, -15]
print(specialFilter(nums1))  # 1

nums2 = [33, -2, -3, 45, 21, 109]
print(specialFilter(nums2))  # 2
```

The function `specialFilter` iterates through the input `nums` and checks if each number greater than 10 has both the first and last digits odd. The total count of such numbers is then returned. The provided test cases demonstrate the function's behavior for illustrative purposes.