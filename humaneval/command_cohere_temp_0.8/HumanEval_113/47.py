```python
def odd_count(lst):
    r = []
    for i, s in enumerate(lst, start=1):
        n = sum(1 for c in s if c % 2 == 1)
        r.append(f"the number of odd elements in the string {i} of the input is {n}")
    return r
```

The code uses a simple `for` loop to iterate through each string in the list and calculate the number of odd digits. The `enumerate` function is used to assign a unique index to each string for correct positioning in the output list. Using a `sum` function with a generating expression, it counts the number of odd digits in each string. Finally, the result is formatted into a string to produce the desired output.