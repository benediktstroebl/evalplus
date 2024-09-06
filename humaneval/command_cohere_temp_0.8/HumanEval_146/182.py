```python
def specialFilter(nums):
    oddFirsts = [num for num in nums if int(num[0]) % 2 == 1]
    oddLasts = [num for num in nums if int(num[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The Python script defines a function `specialFilter` that takes an array of numbers as input and returns the number of elements in the array that meet the following criteria:
- First and last digits of the number must be odd (1, 3, 5, 7, 9).

The function filters the input array `nums` to create two separate lists: `oddFirsts` and `oddLasts`, which contain numbers that have odd first and last digits, respectively. 

The script then uses the bitwise `&` operator to find the common elements between `oddFirsts` and `oddLasts` to identify the numbers that meet both criteria. The function finally returns the length of this filtered list. 

This solution is efficient and straightforward, providing the correct count of numbers that meet the given odd first and last digits criteria in the input array.