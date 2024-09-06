```python
def specialFilter(nums):
    oddFirsts = [num for num in nums if int(num[0]) % 2 == 1]
    oddLasts = [num for num in nums if int(num[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The above code uses Python's list comprehension and logical operators to determine the count of numbers that fit the given criteria. The `&` operator returns elements that are present in both oddFirsts and oddLasts, ensuring that the first and last digits are odd. This solution has an efficiency of O(n) time complexity, where n is the length of the input list "nums". It takes linear time to check every digit of each element in the list.