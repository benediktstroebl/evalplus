```python
def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            currentDigits = [int(digit) for digit in str(num)]
            if currentDigits[0] % 2 == 1 and currentDigits[-1] % 2 == 1:
                oddCount += 1
    return oddCount
```

This Python script defines a function called `specialFilter` that takes a list of numbers as input and counts the number of elements in the list that meet a specific criteria:
1. The number is greater than 10 (i.e., positive integers larger than 10).
2. The first and last digits of the number are odd (1, 3, 5, 7, or 9).

The function iterates through each number in the input list and checks if the number satisfies both conditions. If it does, the `oddCount` variable is incremented. Finally, the function returns the count of numbers that meet these odd first and last digits criteria.