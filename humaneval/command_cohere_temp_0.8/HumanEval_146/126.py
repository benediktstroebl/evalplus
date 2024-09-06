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

The function `specialFilter` uses a loop to iterate through each number in the input `nums` array. For each number, it checks if the number is greater than 10. If so, it extracts the first and last digits of the number using string manipulation and checks if both digits are odd (1, 3, 5, 7, or 9). If both digits are odd, it increments the `oddCount` variable, which keeps track of the count of numbers that satisfy this condition. Finally, the function returns the `oddCount`. 

Let's break down the code step by step:
1. `oddCount = 0`: Initially, the count of numbers with odd first and last digits is set to 0. 
2. `for num in nums:`: The loop iterates through each element in the input array `nums`. 
3. `if num > 10:`: This condition checks if the current number `num` is greater than 10, as the problem statement requires. If this is the case, it means that the first digit of the number must be different from 1-10, and the last digit must be different from 0-9, as these digits can only be 1, 3, 5, 7, or 9.
4. `firstDigit = int(str(num)[0])`: Here, the first character of the string representation of the number `num` is converted to an integer. This effectively extracts the first digit of the number. 
5. `lastDigit = int(str(num)[-1])`: This part extracts the last digit of the number by accessing the last character of the string representation of the number. 
6. ` if firstDigit % 2 == 1 and lastDigit % 2 == 1:`: This condition checks if both the first and last digits are odd (1, 3, 5, 7, or 9). It uses the modulo operator `%` to check if the digits are odd, as integers divided by 2 with a remainder of 1 represent odd numbers. 
7. `oddCount += 1`: If the above condition is true, it means that the number satisfies the problem statement's criteria of having both odd first and last digits while being greater than 10. Therefore, the `oddCount` variable is incremented to keep track of such numbers. 
8. After iterating through all numbers in the array, the function returns the `oddCount`, which represents the number of elements in the array that satisfy the given condition. 

The code efficiently solves the problem in a self-contained manner, producing the expected result for the provided test cases and any other input that follows the specified criteria.