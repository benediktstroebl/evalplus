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
1. The number is greater than 10 (i.e., `num > 10`). This ensures that only larger numbers are considered for the odd digit count.
2. Both the first and last digits of the number are odd (1, 3, 5, 7, or 9). This is checked using string manipulation.

Here's how the script works:
1. It initializes a variable `oddCount` to 0, which will keep track of the count of numbers that satisfy the defined condition.
2. It iterates through each element `num` in the input list `nums`.
3. For each number, it checks if the number is greater than 10. If not, it skips to the next number in the list.
4. If the number is greater than 10, it extracts the first digit of the number using string manipulation (`str(num)[0]`), and the last digit using (`str(num)[-1]`).
5. It then checks if both the first and last digits are odd (1, 3, 5, 7, or 9).
6. If the above condition is met, the `oddCount` is incremented by 1.

Finally, the function returns the `oddCount`, which represents the number of elements in the input list that meet the defined criteria.