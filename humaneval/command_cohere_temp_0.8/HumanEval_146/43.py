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
1. The number is greater than 10 (i.e., `num > 10`). 
2. Both the first and last digits of the number are odd (1, 3, 5, 7, or 9). 

The function achieves this by:
- Iterating through each number in the input list.
- Checking if the number satisfies the first condition regarding its magnitude.
- Extracting the first and last digits of the number using string manipulation.
- Checking if the extracted digits are, individually, odd.
- Incrementing a counter if both the conditions are met. 

The provided example in the prompt states that for the list `[15, -73, 14, -15]` the function will return `1` and for the list `[33, -2, -3, 45, 21, 109]` it will return `2`.