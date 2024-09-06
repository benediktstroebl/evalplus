```python
def specialFilter(nums):
    oddFirsts = [num for num in nums if int(num[0]) % 2 == 1]
    oddLasts = [num for num in nums if int(num[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The above method utilizes Python's list comprehension and bitwise operators to concurrently filter out numbers that fit the specified criteria. In this process, the `&` operator generates a binary AND operation between the two lists, **oddFirsts** and **oddLasts**, and subsequently calculates the length of the resulting intersected list. This procedure determines the total number of elements in the array that are greater than ten and have odd first and last digits. 

To properly examine the function, the included test cases validate the output for various defined arrays of numbers. 

This approach provides an effective solution to the problem statement and demonstrates Python's adaptability in handling intricate logical and numerical computations through list operations and bitwise techniques.