```python
def specialFilter(nums):
    oddFirsts = [num for num in nums if int(num[0]) % 2 == 1]
    oddLasts = [num for num in nums if int(num[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The script uses Python's array filtering capabilities along with the `&` operator to find the intersection of the two filtered arrays, which corresponds to the numbers that both meet the first and last digit criteria. The function then returns the count of numbers that satisfy this condition. 

To execute the function and see the results interactively, copy and paste it into a Python interpreter.