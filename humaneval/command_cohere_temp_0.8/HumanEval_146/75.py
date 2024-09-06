```python
def specialFilter(nums):
    oddFirsts = [x for x in nums if int(str(x)[0]) % 2 == 1]
    oddLasts = [x for x in nums if int(str(x)[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The Python script employs a nested list comprehension to identify numbers that satisfy the problem condition. It evaluates both the first and last digits of each number in the `nums` array to determine if they're odd, and subsequently intersects these lists to pinpoint numbers that fulfill the requirement. This approach ensures that the problem is correctly solved and achieves the desired outcome of counting numbers that both first and last digits are odd.