```python
def specialFilter(nums):
    oddFirsts = [x for x in nums if int(x[0]) % 2 == 1]
    oddLasts = [x for x in nums if int(x[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The script uses Python's array filtering functionality and the & operator to find the intersection of the two arrays (oddFirsts and oddLasts). The function then counts the elements in this intersection, which corresponds to the numbers that fulfill the problem's criteria.