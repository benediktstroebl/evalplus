```python
def specialFilter(nums):
    oddFirsts = [x for x in nums if int(x[0]) % 2 == 1]
    oddLasts = [x for x in nums if int(x[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The script employs a binary filter approach, using the & operator to filter the common elements between `oddFirsts` and `oddLasts`. This strategy eliminates the need for a nested list comprehension and enhances performance, ensuring that the primary goal is to pinpoint numbers that fulfill the given criteria.