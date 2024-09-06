```python
def specialFilter(nums):
    odd_digits = [int(digit) for digit in nums if int(digit) % 2 == 1]
    return sum(num for num in nums if len(odd_digits) == 2 and num > 10)
```

The function `specialFilter` uses a list comprehension to create a list of odd digits from the input `nums` and then uses another sum context expression to iterate over the `nums` to check whether the length of the list of odd digits is 2 and the number is greater than 10. The result is the count of numbers satisfying this condition.