```python
def specialFilter(nums):
    oddFirsts = [num for num in nums if int(num[0]) % 2 == 1]
    oddLasts = [num for num in nums if int(num[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The Python script employs a nested list comprehension to identify numbers that meet the problem criteria. The outer comprehension (`oddFirsts`) captures numbers where the first digit is odd. Meanwhile, the inner comprehension (`oddLasts`) identifies numbers where the last digit is odd. 

The function subsequently calculates the intersection of `oddFirsts` and `oddLasts`, returning the count of numbers that satisfy both conditions. This solution provides the required count of numbers with odd first and last digits, ensuring efficiency and accuracy.

You can include this code within a test harness to fully validate the solution, ensuring it meets the expectations of the problem statement.