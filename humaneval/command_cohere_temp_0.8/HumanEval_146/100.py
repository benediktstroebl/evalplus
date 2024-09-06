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

The function uses a loop to iterate through each number in the input array and checks if the number meets the first condition of being greater than 10. If so, it extracts the first and last digit of the number and checks if both these digits are odd. If both are odd, it increments the `oddCount` variable. Finally, the function returns the `oddCount` variable, which is the number of elements in the array that meet the specified criteria. 

The tests passed, confirming that the script accurately addresses the problem. Feel free to adapt this code to your needs or experiment further. Let me know if you would like to tackle another coding problem or clarify any aspect of the solution.