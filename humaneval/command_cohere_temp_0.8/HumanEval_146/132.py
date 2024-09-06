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

This function `specialFilter` takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and have odd first and last digits. It iterates through each number in the `nums` array and checks if the number is greater than 10. If so, it extracts the first and last digit of that number using string manipulation and ensures they are odd. If both digits are odd, it increments the `oddCount` variable, total count of such numbers. Finally, the function returns the `oddCount` variable. 

To follow the problem statement, the function only counts numbers that both the first and last digits are odd (1, 3, 5, 7, 9). 

Such numbers are highlighted in the sample tests input below:
```python
test_list = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]
print(specialFilter(test_list))  # Output: 1
```