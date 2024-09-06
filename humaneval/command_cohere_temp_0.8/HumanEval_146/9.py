```python
def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            currentDigitValue = int(str(num)[0])
            lastDigitValue = int(str(num)[-1])
            if currentDigitValue % 2 == 1 and lastDigitValue % 2 == 1:
                oddCount += 1
    return oddCount

# Tests
nums = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]
print(specialFilter(nums))  # 1 2
```

The function `specialFilter` iterates through the input list of numbers, checking if each number greater than 10 has both the first and last digits odd. The `oddCount` variable keeps track of how many numbers in the array satisfy this condition. The provided test case should yield the output `1 2`.