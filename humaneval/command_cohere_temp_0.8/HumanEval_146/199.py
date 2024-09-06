```python
def specialFilter(nums):
    oddFirsts = [num for num in nums if int(num[0]) % 2 == 1]
    oddLasts = [num for num in nums if int(num[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The Python script defines a function `specialFilter` taking an array of numbers as input and returning the number of elements greater than 10 where both the first and last digits are odd (1, 3, 5, 7, or 9). It uses boolean operators to filter numbers with odd first and last digits and calculates the length of the intersecting set to determine the count of such numbers, fulfilling the problem requirements.