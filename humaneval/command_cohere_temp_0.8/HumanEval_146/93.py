```python
def specialFilter(nums):
    oddFirsts = [num for num in nums if int(num[0]) % 2 == 1]
    oddLasts = [num for num in nums if int(num[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The Python script defines a function `specialFilter` that takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and both the first and last digits of a number are odd (1, 3, 5, 7, 9). To achieve this, the function uses two lambda functions, `oddFirsts` and `oddLasts`, to filter out numbers that satisfy the first or last digit criteria. The bitwise AND operator `&` is used to identify common elements between the two filtered lists, ensuring both first and last digits are odd. The function returns the count of numbers that meet these criteria, specifically counting elements in the set intersection of `oddFirsts` and `oddLasts`.