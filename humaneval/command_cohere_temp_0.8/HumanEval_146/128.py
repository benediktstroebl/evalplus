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

This Python script defines a function called `specialFilter` that takes a list of numbers as input and counts the number of elements in the list that meet a certain criteria:
1. It iterates through each element `num` in the input list `nums`.
2. If the number is greater than 10, it extracts the first digit and the last digit of the number.
3. It then checks if both the first and last digits are odd (i.e., their remainder when divided by 2 is equal to 1).
4. If the condition is met, it increments the `oddCount` variable by 1.
5. Finally, it returns the `oddCount` variable, which represents the number of elements in the list that satisfy the defined condition. 

The script effectively solves the problem as explained in the example tests provided earlier.