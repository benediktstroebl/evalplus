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

This function `specialFilter` takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and have odd first and last digits. It loops through each number in the `nums` array and checks if the number is greater than 10. If so, it extracts the first and last digit of that number using string manipulation and ensures they are odd. If both digits are odd, it increments the `oddCount` variable, which is used to keep track of the count of numbers meeting these criteria. Finally, the function returns the `oddCount`. 

This solution adheres to the problem statement and provides the specified count of numbers satisfying the given conditions.