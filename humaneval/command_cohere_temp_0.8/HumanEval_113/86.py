```python
def odd_count(lst):
    r = []
    for idx, s in enumerate(lst):
        n = sum(1 for c in s if c % 2 == 1)
        r.append(f"the number of odd elements in the string {idx + 1} of the input is {n}")
    return r
```

The Python script defines a function `odd_count` that takes a list of strings as input. It iterates through each string in the list and counts the number of odd digits in each string using a generator expression. Then, it generates a string that contains the count of odd digits in each string and appends it to a list `r`. The final result is a list of these generated strings, which provides the count of odd digits in each string in the input list.