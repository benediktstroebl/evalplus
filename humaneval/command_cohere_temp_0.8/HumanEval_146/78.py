```python
def specialFilter(nums):
    oddDigits = [x for x in nums if x > 10 and int(str(x)[0]) % 2 == 1 and int(str(x)[-1]) % 2 == 1]
    return len(oddDigits)
```

This Python script defines a function called `specialFilter` that takes a list of numbers as input and returns the number of elements in the list that meet the following criteria:
- Greater than 10 (`x > 10`)
- The first digit (indexed at 0) of the decimal representation of the number (`int(str(x)[0])`) is odd (`% 2 == 1`)
- The last digit of the decimal representation of the number (`int(str(x)[-1])`) is odd (`% 2 == 1`)

The list comprehension `oddDigits` creates a list of all the numbers from `nums` that satisfy all these conditions. The function then returns the length of this `oddDigits` list, which is the number of elements in the input list that meet the specified criteria.