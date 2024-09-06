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

This Python script defines a function called `specialFilter` that takes a list of numbers as input and calculates the number of elements in the list that meet a specific criteria:
1. The element is greater than 10 (i.e., it's not just a single digit).
2. Both the first and last digits of the number are odd (1, 3, 5, 7, or 9).

The function iterates through each element in the input list using a `for` loop. It checks if the number is greater than 10 using `int(str(num)[0])` to get the first digit and `int(str(num)[-1])` to get the last digit. If both the first and last digits are odd, it increments the `oddCount` variable.

Finally, the function returns the value of `oddCount`, which represents the number of elements in the input list that satisfy the defined condition.