```python
def odd_count(lst):
    r = []
    for i, s in enumerate(lst, start=1):
        n = sum(int(d) % 2 == 1 for d in s)
        r.append(f"the number of odd elements in the string {i} of the input." if n == 1 else f"{n}n the string {i} of the input.")
    return r
```

The solution leverages Python's `enumerate` to iterate through the list of strings and calculate the number of odd elements for each string. The `sum` function is used within a generator expression to determine the count of odd digits in each string, and `enumerate` helps assign each string a corresponding index for output. The result is a list of appropriately formatted strings, as specified in the problem statement.