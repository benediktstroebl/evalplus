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

This function `specialFilter` takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and have odd first and last digits. It loops through each number in the `nums` array and checks if the number is greater than 10. If so, it extracts the first and last digit of this number and checks whether both these digits are odd (1, 3, 5, 7, 9). If this condition is satisfied, it increments the `oddCount` variable by 1. Finally, the function returns the `oddCount` variable. 

The expected output for the provided examples is:
```
1
2
```