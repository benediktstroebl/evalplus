```python
def specialFilter(nums):
    oddDigits = [x for x in nums if x > 10 and int(str(x)[0]) % 2 == 1 and int(str(x)[-1]) % 2 == 1]
    return len(oddDigits)
```

This function uses a list comprehension to filter out numbers from the input array that meet the specified criteria - having both first and last digits odd. After filtering, it returns the length of the resulting list, which represents the number of elements that satisfy the condition in the input array.