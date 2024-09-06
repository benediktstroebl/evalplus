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

This function `specialFilter` takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and both the first and last digits of a number are odd (1, 3, 5, 7, 9). The function uses a for loop to iterate through each number in the `nums` array and checks if the number is greater than 10. If so, it extracts the first and last digit of that number using string manipulation, and checks if both these digits are odd. If this condition is met, the count is incremented by 1. The final count of such numbers is returned. 

To follow the problem statement exactly, the code assumes that the input array contains only positive numbers and therefore does not handle negative cases, as the penalty of handling such cases would be unnecessarily burdensome for this specific problem. The code also does not have any explicit unit tests, as self-containment was requested; however, it is fairly straightforward and should be easy to verify against the described problem statement.