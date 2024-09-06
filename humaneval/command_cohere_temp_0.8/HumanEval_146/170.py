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
```

This Python script defines a function called `specialFilter` that takes a list of numbers as input and calculates the number of elements in the list with the condition that the number is greater than 10 and both the first and last digits of the number are odd (1, 3, 5, 7, or 9). The function uses a `for` loop to iterate through each element in the input list and checks if the number is greater than 10. If so, it extracts the first and last digits of the number, and if both are odd, it increments the `oddCount` variable. Finally, the function returns the calculated count of numbers that meet the specified condition.