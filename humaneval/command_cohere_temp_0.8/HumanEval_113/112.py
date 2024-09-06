```python
def odd_count(lst):
    r = []
    for digits in lst:
        count = sum(1 for digit in digits if digit % 2 == 1)
        r.append(f"the number of odd elements in the string {count} of the input")
    return r
```

The code leverages Python's `sum` function, along with a generator expression, to efficiently calculate the count of odd digits in each string. This expression repeatedly examines each digit, determining whether it is odd, and increments the total count when this is the case. The result is a concise and effective solution to the problem.