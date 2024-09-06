```python
def specialFilter(nums):
    oddFirsts = [x for x in nums if int(str(x)[0]) % 2 == 1]
    oddLasts = [x for x in nums if int(str(x)[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The above code uses Python's list comprehension to filter elements that have odd first digits and odd last digits, and finally uses the bitwise `&` operator to find the common elements between these two lists. This will be our result. The code then returns the length of this intersection.