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

This function `specialFilter` takes an array of numbers (`nums`) as input and counts the number of elements in the array that meet the following criteria:
1. The number is greater than 10.
2. The first and last digits of the number are odd (1, 3, 5, 7, or 9).

The function uses a for loop to iterate through each element in the input array and checks if the element is greater than 10. Then it extracts the first and last digit of the number to determine if they are odd. If both are odd, it increments the `oddCount` variable. Finally, the function returns the `oddCount` variable, which is the number of elements in the array that meet the specified criteria. 

This solution adheres to the problem statement and provides the desired output for the given test cases.