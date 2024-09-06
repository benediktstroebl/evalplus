```python
def specialFilter(nums):
    oddFirsts = [num for num in nums if int(num[0]) % 2 == 1]
    oddLasts = [num for num in nums if int(num[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The Python script employs a nested list comprehension to identify numbers that satisfy the problem condition. Specifically, the function `specialFilter` accepts an array of numbers, termed `nums`. It subsequently employs the list comprehension `oddFirsts` to pinpoint numbers within `nums` where the initial digit is odd. This comprehension yields a new list that accommodates these odd-first numbers.

Similarly, a second list comprehension, `oddLasts`, is employed to identify numbers in `nums` where the final digit is odd. This list comprehension also results in a new list, this time featuring odd-last numbers.

The function proceeds to perform a set intersection, denoted `&`, between `oddFirsts` and `oddLasts`. This operation eliminates duplicate numbers and yields a unique set of numbers from both list comprehensions. The function finally calculates the length of this resulting set, which corresponds to the number of elements in the original array that fulfill the provided condition.