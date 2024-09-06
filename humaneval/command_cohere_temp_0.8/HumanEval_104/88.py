```python
def unique_digits(x):
    odd = [int(''.join(c for c in str(i) if c % 2 != 0)) for i in x if int(''.join(c for c in str(i) if c % 2 != 0)) <= 999999]
    return sorted(odd)
```

The function `unique_digits` takes a list of positive integers `x` as its argument and returns a sorted list of all elements that do not have any even digits. To do this, it creates a list called `odd` that contains all integers that do not have any even digits using a list comprehension. The condition `c % 2 != 0` filters out all even digits when converting an integer to a string and back to an integer. Finally, it returns a sorted list of integers in `odd` with a maximum value of 999999 to cover all possible integers for this task.