```python
def specialFilter(nums):
    oddFirsts = [num for num in nums if int(num[0]) % 2 == 1]
    oddLasts = [num for num in nums if int(num[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The above code uses Python's list comprehension to filter numbers with odd first digits (`int(num[0]) % 2 == 1`) and odd last digits (`int(num[-1]) % 2 == 1`). It then uses the bitwise operator `&` to find the common elements between these two lists and thereby return the numbers that both meet the given criteria. The function returns the length of this resulting list.