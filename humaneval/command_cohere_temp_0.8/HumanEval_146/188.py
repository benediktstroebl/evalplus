```python
def specialFilter(nums):
    oddFirsts = [num for num in nums if int(num[0]) % 2 == 1]
    oddLasts = [num for num in nums if int(num[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The script employs a logical AND operation between two lists, `oddFirsts` and `oddLasts`, to efficiently filter out the numbers from the array that meet the specified criteria. The AND operation returns a list that has elements that are present in both oddFirsts and oddLasts, which effectively filters the numbers with both odd first and last digits. Finally, the `len()` function is used to determine the number of elements in the resulting list, which is the number of numbers that satisfy the odd first and last digits criterion.