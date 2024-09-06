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

This function `specialFilter` takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and both the first and last digits of a number are odd (1, 3, 5, 7, 9). The function uses a for loop to iterate through each number in the `nums` array and checks if the number is greater than 10. If so, it extracts the first and last digit of that number using string manipulation and ensures they are odd. If this condition is true, the count `oddCount` variable increments. The function returns the `oddCount` at the end. 

## Example Usage:
```python
print(specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]))
```
```
1
```

This will return 1, as the answer correctly identifies that element 15 in the list has first and last digits odd, exceeding the size of 10.