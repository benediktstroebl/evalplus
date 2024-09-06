```python
def specialFilter(nums):
    oddFirsts = [num for num in nums if int(num[0]) % 2 == 1]
    oddLasts = [num for num in nums if int(num[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The Python script employs a nested list comprehension to identify numbers that satisfy the problem condition. Specifically, the comprehension for `oddFirsts` short-circuits and produces an empty list if it finds a number not starting with a digit odd, thus skipping the rest of the iteration. This optimized approach prevents duplicative work across list comprehensions.

The `&` operator is then used to find the common elements between `oddFirsts` and `oddLasts`. This results in the list of numbers that both fulfill the odd first digit and odd last digit conditions. The function ultimately returns the count of these common elements.