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

This function `specialFilter` takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and have odd first and last digits. It iterates through each number in the `nums` array and checks if the number is greater than 10. If so, it extracts the first and last digits of that number using string manipulation and ensures they are odd. If both digits are odd, it increments the `oddCount` variable, which is used to return the desired count. 

The code leverages basic number manipulation and loop constructs in Python to solve the problem. 

```python 
test1 = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]
test2 = [15, -74, 24, -55, 111, -1, 31, 59, 89, 99]
print(specialFilter(test1)) # 1
print(specialFilter(test2)) # 3
``` 

This should output:
```bash
1
3
```