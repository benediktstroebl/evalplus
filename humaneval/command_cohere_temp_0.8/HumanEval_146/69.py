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
print(f'Test Case 1 -> {specialFilter(nums1)}')

nums2 = [33, -2, -3, 45, 21, 109]
print(f'Test Case 2 -> {specialFilter(nums2)}')
```

The function `specialFilter` goes through each number in the `nums` array. It checks if the number is greater than 10 and if so, it evaluates the first and last digits of that number by converting it to a string, extracting the first and last digits, and converting them back to integers for the modulus operation. If both digits are odd, it increments the `oddCount` variable by 1. Finally, it returns the variable `oddCount`, which counts the number of numbers with both first and last digits odd and greater than 10. 

The output of the code above is:
```bash
Test Case 1 -> 1
Test Case 2 -> 2
```