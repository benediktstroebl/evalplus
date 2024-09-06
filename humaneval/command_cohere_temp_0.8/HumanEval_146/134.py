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
1. They must be greater than 10. 
2. The first and last digits of the numbers should be odd (1, 3, 5, 7, or 9). 

The function uses a `for` loop to iterate through each element in the `nums` array and checks if the number is greater than 10. If true, it extracts the first and last digit of the number using string manipulation, and then checks if both these digits are odd. If both are odd, it increments the `oddCount` variable by 1. Finally, the function returns the `oddCount`, which is the number of numbers in the array that meet the specified criteria. 

This solution adheres to the problem description and provides a clear and concise implementation demonstrating Python best practices. Let me know if you would like me to explain any of the steps taken in this code further, or provide any further optimizations or enhancements. 
You can also copy and paste this code into a local Python environment to further experiment and test the function. From there, you can expand the testing suite to include different cases and edge scenarios to further validate its robustness.