```python
def specialFilter(nums):
    odd_digits = [int(i) for i in nums if i % 2 != 0 and int(i) % 10 != 0]
    return len(odd_digits)
```

The function `specialFilter` uses a list comprehension to filter out numbers from the array `nums` that have odd digits in the tens place (`i % 10 != 0`) and overall (`i % 2 != 0`) place. The length of this filtered list is then returned, which represents the number of elements in the array that meet the given criteria.