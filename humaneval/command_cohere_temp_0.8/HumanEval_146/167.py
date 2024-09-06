```python
def specialFilter(nums):
    oddFirsts = [x for x in nums if int(x[0]) % 2 == 1]
    oddLasts = [x for x in nums if int(x[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The script employs a logical `AND` operator (`&`) between two sets to find the overlapping elements. Here's a breakdown of each part:
1. `oddFirsts` is a list of numbers where the first digit is odd. This list is created using a list comprehension with a condition: `int(x[0]) % 2 == 1`. For example, if the number is '15', `int(15[0]) % 2 == 1` is evaluated to True, and it's included in the list.
2. `oddLasts` is a list of numbers where the last digit is odd. This list is also created using a list comprehension with a similar condition: `int(x[-1]) % 2 == 1`. For the number '15', `int(15[-1]) % 2 == 1` is True, and it's included in this list.
3. The length of elements common in both `oddFirsts` and `oddLasts` is returned as the solution.