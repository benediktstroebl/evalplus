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
1. The number is greater than 10 (i.e., it exceeds the threshold provided in the problem).
2. The first and last digits of the number are odd (1, 3, 5, 7, or 9).

The function iterates through each number in the input list using a `for` loop. It first checks if the number is greater than 10 using `num > 10`. Then, it extracts the first and last digits of the number using string manipulation. The `str(num)[0]` retrieves the first digit and `str(num)[-1]` retrieves the last digit when converted to a string.

Finally, the function checks if the first and last digits are odd using the modulo `% 2 == 1` and increments the `oddCount` variable if both conditions are met. The function then returns the `oddCount`, which represents the number of elements in the list that satisfy the defined condition.