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

This function `specialFilter` takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and have odd first and last digits. It iterates through each number in the `nums` array and checks if the number is greater than 10. If so, it extracts the first and last digits of that number using string manipulation and ensures they are odd. If both digits are odd, it increments the `oddCount` variable, which is used to keep track of the count of numbers meeting this criterion. Finally, the function returns the value of `oddCount`. 

You can include this code inside a markdown code block, as you originally requested, to provide a self-contained solution to the problem statement. 
If you'd like to test this function, you can write a test case in the same file, outside the function, and use an appropriate assertion, like so: 
```python
test_cases = [
    [15, -73, 14, -15, 33, -2, -3, 45, 21, 109],
    [20, 101, 65, 94, 77, 50, 74, 33, 58, 19],
]

expected_results = [1, 2]

for i in range(len(test_cases)):
    nums = test_cases[i]
    result = specialFilter(nums)
    assert result == expected_results[i]
``` 

This will automatically validate the function's behavior against the test cases provided.