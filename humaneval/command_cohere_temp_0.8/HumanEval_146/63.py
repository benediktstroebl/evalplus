```python
def specialFilter(nums):
    oddFirsts = [x for x in nums if int(str(x)[0]) % 2 == 1]
    oddLasts = [x for x in nums if int(str(x)[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The script uses Python's filtering capabilities and the & operator to combine two sets while eliminating duplicates. Let's break down the code:
1. `oddFirsts` is a list of numbers where the first digit is odd, and is created using a list comprehension with the condition `int(str(x)[0]) % 2 == 1`.
2. `oddLasts` is a list of numbers where the last digit is odd, and is created using a list comprehension with the condition `int(str(x)[-1]) % 2 == 1`.
3. The `&` operator is a binary operator that returns the intersection of two sets, which in this case is the list of numbers that are both sorts of odd at the first and last digits.
4. The final length of the resulting intersection set gives the required count.