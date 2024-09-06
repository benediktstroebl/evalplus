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

This Python script defines a function called `specialFilter` that takes a list of numbers as input and calculates the number of elements in the list with the condition that the number is greater than 10 and both the first and last digits of its digits are odd (1, 3, 5, 7, 9). 

The function then iterates through each number in the list and checks if it meets the condition, and increments the `oddCount` variable if it does. Finally, the function returns the `oddCount` variable, which represents the number of numbers in the list that meet the specified condition. 

The script self-contained and doesn't require any import statements, making it portable and easy to execute.