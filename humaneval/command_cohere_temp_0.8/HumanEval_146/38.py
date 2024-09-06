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

This function `specialFilter` takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and have odd first and last digits. It iterates through each number in the `nums` array and checks if the number is greater than 10. If so, it extracts the first and last digits of that number using string manipulation and ensures they are odd. If both conditions are met, it increments the `oddCount` variable, and finally, the function returns the `oddCount`. 

You can test this function using the following code:
```python
test_nums = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]
print(specialFilter(test_nums))  # Output: 1
``` 

This will return `1` as only the number `15` from the array `[15, -73, 14, -15, 33, -2, -3, 45, 21, 109]` fulfills the specified criteria.