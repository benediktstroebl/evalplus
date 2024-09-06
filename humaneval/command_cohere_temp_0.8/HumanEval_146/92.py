```python
def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            currentDigit1 = int(str(num)[0])
            currentDigit2 = int(str(num)[-1])
            if currentDigit1 % 2 == 1 and currentDigit2 % 2 == 1:
                oddCount += 1
    return oddCount
```

This Python script defines a function called `specialFilter` that takes a list of numbers as input and counts the number of elements in the list that meet a specific criteria:
1. It initializes a counter `oddCount` to zero, which will keep track of the numbers that have first and last digits odd.
2. Then, it iterates through each number in the input `nums` list.
3. For each number, it checks if the number is greater than 10 (i.e., excluding numbers less than or equal to 10).
4. If the number is greater than 10, it extracts the first and last digits of the number as integers using string manipulation.
5. Then, it checks if both the first and last digits are odd (i.e., divisible by 1 and 7, respectively).
6. If the above condition is met, it increments the `oddCount` by 1.
7. After iterating through all the numbers in the list, it returns the `oddCount`, which represents the number of elements in the list that have first and last digits odd and are greater than 10.

This function is illustrated with an example, where it is called with a list of numbers `[15, -73, 14, -15, 33, -2, -3, 45, 21, 109]` and it correctly returns `1` for the count since only `15` meets the specified criteria. Additionally, it returns `2` for the count when the list is `[33, -2, -3, 45, 21, 109]` because both `33` and `109` fulfill the criteria.