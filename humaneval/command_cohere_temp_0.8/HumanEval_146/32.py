```python
def specialFilter(nums):
    oddCounts = 0
    for num in nums:
        if num > 10:
            currentDigit = int(str(num)[0])
            lastDigit = int(str(num)[-1])
            if currentDigit % 2 == 1 and lastDigit % 2 == 1:
                oddCounts += 1
    return oddCounts
```

This function `specialFilter` takes an array of numbers (`nums`) as input and counts the number of elements in the array that meet the specified criteria. It iterates through each number in the `nums` array and checks if the number is greater than 10. If so, it extracts the first and last digits of that number using string manipulation and checks if both these digits are odd (1, 3, 5, 7, or 9). Finally, it counts the numbers with odd first and last digits that are greater than 10 and returns the count. 

The total time complexity of this code is `O(n log n)`, where `n` represents the amount of elements in the array. This is due to the fact that the check of whether a number is greater than 10 includes a comparison and a call to `len()` which both take `O(1)` time, while each iteration of the loop takes `O(log n)` to access the elements in the array.

The memory complexity is `O(n)` due to the loop iterating through the array and storing information in the `oddCounts` variable.