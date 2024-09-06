```python
def specialFilter(nums):
    oddFirsts = [num for num in nums if int(num[0]) % 2 == 1]
    oddLasts = [num for num in nums if int(num[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The Python script defines a function `specialFilter` that takes an array of numbers as input and returns the number of elements in the array that meet the following criteria:
- First and last digits of the number are odd (1, 3, 5, 7, or 9).

The function filters the input array `nums` using two nested list comprehensions. One comprehension filters numbers based on their first odd digit, and the other filters numbers based on their last odd digit. The length of the intersection of these two filtered lists gives the desired count. The function solves the problem as described in the prompt.