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

This function `specialFilter` takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and have odd first and last digits. It iterates through each number in the `nums` array and checks if the number is greater than 10. If so, it extracts the first and last digit of that number using string manipulation, and then checks if both these digits are odd. If this condition is met, it increment the `oddCount` variable by 1. Finally, the function returns the count of such numbers. 

To see the behavior of the function, you can run the following code:
```python
test_nums = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]
print(specialFilter(test_nums))  # Output: 1 2
```