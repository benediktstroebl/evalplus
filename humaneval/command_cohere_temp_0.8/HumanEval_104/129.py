```python
def unique_digits(x):
    odd = [int(''.join(c for c in str(n) if c % 2 != 0)) for n in x if int(''.join(c for c in str(n) if c % 2 != 0)) <= n]
    return sorted(odd)
```

The function `unique_digits` uses a list comprehension to iterate through each element in the input list `x`. It converts each element to a string, removes even digits using a conditional expression, and then converts it back to an integer. 

These processed integers are then stored in the `odd` list, and finally, the function returns a sorted version of this list. The sorting step ensures that the returned list is ordered from smallest to largest. 

The conditional expression `c % 2 != 0` evaluates to `True` if a character is odd, meaning that it will filter out all even digits.