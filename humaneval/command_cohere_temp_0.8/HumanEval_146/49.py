```python
def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            currentDigit = int(str(num)[0])
            lastDigit = int(str(num)[-1])
            if currentDigit % 2 == 1 and lastDigit % 2 == 1:
                oddCount += 1
    return oddCount
```

This function `specialFilter` takes an array of numbers (`nums`) as input and counts the number of elements in the array that meet the following criteria:
1. They must be greater than 10. 
2. The first and last digits of the number should be odd (1, 3, 5, 7, or 9). 

The function uses a `for` loop to iterate through each element in the `nums` array and checks if the element is greater than 10. If true, it extracts the first and last digits of the number using string manipulation, and then checks if both these digits are odd. If both are indeed odd, it increments the `oddCount` variable by 1. Finally, it returns `oddCount`, which holds the number of elements in the array that satisfy the specified criteria. 

This solution adheres to the problem statement and provides the desired output for the given test cases. Plese let me know if any additional requirements or if you would like to see more test cases to ensure robustness of the solution.