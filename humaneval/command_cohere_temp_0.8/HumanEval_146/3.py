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
```

This function `specialFilter` takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and where both the first and last digits of a number are odd (1, 3, 5, 7, 9). The function uses a for loop to iterate through each number in the `nums` array and checks if the number is greater than 10. If so, it extracts the first and last digits of the number using string slicing (`str(num)[0]` and `str(num)[-1]`), and determines whether these digits are odd using the modulo operator (`% 2 == 1`). If both digits are odd, it increments the `oddCount` variable by 1. Finally, the function returns `oddCount`, which represents the number of numbers meeting the specified criteria in the input array.