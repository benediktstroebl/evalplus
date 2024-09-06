```python
def specialFilter(nums):
    oddFirsts = [x for x in nums if int(str(x)[0]) % 2 == 1]
    oddLasts = [x for x in nums if int(str(x)[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The script employs a logical `AND` operator (`&`) to filter numbers that satisfy both conditions (first and last digits are odd). The resulting length of this common set corresponds to the number of elements that fulfill the given problem statement. 

This approach provides a concise solution to the given problem. It eliminates the need for explicit set unions and memberships and simplifies the filtering process.