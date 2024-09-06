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

This Python script defines a function called `specialFilter` that takes a list of numbers as input and calculates the number of elements in the list with the condition that the number is greater than 10 and both the first and last digits of the number are odd (1, 3, 5, 7, or 9). The function uses a for loop to iterate through each element in the input list and checks if the number is greater than 10. If so, it extracts the first and last digits of the number using string manipulation and uses an integer conversion. It then checks if both these digits are odd using the modulo operation (`% 2 == 1`). 

For example, given the input list `[15, -73, 14, -15]` the function will return `1` because only element `15` satisfies the given condition. Conversely, for the input list `[33, -2, -3, 45, 21, 109]` the function will return `2`, as elements `33` and `109` meet the criteria. The script returns the count of numbers satisfying this condition as the output. 

The code is self-contained and does not rely on any external variables or functions, making it easy to incorporate into larger programs or scripts as needed.