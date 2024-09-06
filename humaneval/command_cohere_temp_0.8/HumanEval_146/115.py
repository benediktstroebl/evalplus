```python
def specialFilter(nums):
    oddFirsts = [num for num in nums if int(num[0]) % 2 == 1]
    oddLasts = [num for num in nums if int(num[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The script uses Python's array filtering functionality along with the & operator to find the intersection of the two arrays. The function then returns the length of the resulting array, which corresponds to the number of elements that satisfy the given criteria.