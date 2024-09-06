```python
def specialFilter(nums):
    oddCounts = 0
    for num in nums:
        if num > 10:
            firstDigit = int(str(num)[0])
            lastDigit = int(str(num)[-1])
            if firstDigit % 2 == 1 and lastDigit % 2 == 1:
                oddCounts += 1
    return oddCounts
```

The solution uses a basic loop to iterate through each number in the array and determines whether the number is greater than 10 and has odd first and last digits. If so, the counter `oddCounts` is increased. Ultimately, the function returns the value of `oddCounts`, which is the number of elements in the array that meet the specified criteria.