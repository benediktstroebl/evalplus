```python
def specialFilter(nums):
    oddCounts = 0
    for num in nums:
        if num > 10:
            currentDigitValue = int(str(num)[0])
            lastDigitValue = int(str(num)[-1])
            if currentDigitValue % 2 == 1 and lastDigitValue % 2 == 1:
                oddCounts += 1
    return oddCounts
```

This Python script defines a function called `specialFilter` that takes a list of numbers as input and counts the number of elements in the list that meet a specific criteria:
1. The number is greater than 10 (i.e., `num > 10`).
2. Both the first and last digits of the number are odd (1, 3, 5, 7, or 9). 

The function achieves this by iterating through each number in the input list. If the number satisfies the criteria, it increments the `oddCounts` variable, which keeps track of the count. Finally, the function returns the value of `oddCounts`, which represents the number of numbers in the list that satisfy the defined condition. 

This solution is both efficient and readable, directly addressing the problem statement's requirements. It's also decoupled from any specific testing framework, making it easy to verify using standard Python list assertions.