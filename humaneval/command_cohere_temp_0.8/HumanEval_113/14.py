```python
def odd_count(lst):
    r = []
    for i, s in enumerate(lst, 1):
        n = sum(1 for c in s if c % 2 == 1)
        r.append(f"the number of odd elements in the string {i} of the input is {n}")
    return r
```

The code leverages Python's built-in `enumerate` to provide the string index (1-indexed) and the string itself in each iteration for the list of strings provided. The `sum` along with a generator expression is used to count the number of odd elements in each string. Then, in the odd_count function, the string index and corresponding odd count are appended to a list to be returned as the final output.