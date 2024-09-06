```python
def specialFilter(nums):
    oddDigits = ['1', '3', '5', '7', '9']
    result = sum(1 for num in nums if int(num) > 10 and 
                 (oddDigits.index(str(num)[0]) != -1 or 
                  oddDigits.index(str(num)[-1]) != -1))
    return result
```

The function `specialFilter` uses a list comprehension that iterates over each number in the input array `nums`. For each number, it checks if the number is greater than 10 and evaluates whether the first or last digit of the number belongs to the list of odd digits (`oddDigits`). The sum function then adds up the occurrences that satisfy this condition to return the final result.