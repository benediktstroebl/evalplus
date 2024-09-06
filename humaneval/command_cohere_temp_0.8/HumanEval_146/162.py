```python
def specialFilter(nums):
    oddFirsts = [x for x in nums if int(str(x)[0]) % 2 == 1]
    oddLasts = [x for x in nums if int(str(x)[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The script employs a logical operator, the intersection (`&`), to find numbers that satisfy both conditions, odd first and last digits. The function filters the list through two nested list comprehensions that check for odd first and last digits, respectively. Ultimately, it returns the count of numbers that satisfy both conditions. This solution is concise and efficient, leveraging Python's list comprehension and logical operators.