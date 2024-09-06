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
1. The number is greater than 10 (i.e., it's not just a single digit).
2. Both the first and last digits of the number are odd (1, 3, 5, 7, or 9).

The function iterates through each number in the input list and checks if it satisfies both conditions. If it does, it increments the `oddCount` variable. Finally, the function returns the count of numbers that meet these criteria.

This solution is efficient and correctly returns the required counts as outlined in the example. It's structured and stylized to be easily understood and adheres to best practices in Python development. You can now use this function to solve the problem consistently and accurately for any given list of numbers.