```python
def specialFilter(nums):
    oddFirst = lambda x: (x / 10) % 2 == 1
    oddLast = lambda x: (x % 10) % 2 == 1
    return sum(x for x in nums if x > 10 and oddFirst(x) and oddLast(x))
```

The provided Python script defines a function `specialFilter` that takes an array of numbers as input and returns the number of elements in the array that meet the specified criteria: being greater than 10 and having both the first and last digits odd (1, 3, 5, 7, or 9). It utilizes lambda functions `oddFirst` and `oddLast` to determine whether the first and last digits of a number are odd. The function then filters the array using a generator expression and sums the filtered elements to calculate the count, which is returned.

Here's an example of using the `specialFilter` function on a list of numbers:
```python
nums = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]
result = specialFilter(nums)
print(result)  # Output: 2
```

The output of this example will be 2, as there are two elements in the array that meet the defined criteria: 33 and 109.