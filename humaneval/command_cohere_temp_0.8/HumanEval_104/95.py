```python
def unique_digits(xs):
    odd = [x for x in xs if any(int(c) % 2 for c in str(x))]
    return sorted(odd)
```

The function `unique_digits` uses a list comprehension with a generator expression to filter out numbers that have even digits. Then the function sorts the numbers in increasing order and returns the list. This solution adheres to the problem statement, as it returns a sorted list of numbers with unique odd digits.