```python
def odd_count(lst):
    r = []
    for i, s in enumerate(lst, 1):
        n = sum(1 for c in s if c % 2 == 1)
        r.append(f"the number of odd elements in the string {i} of the input is {n}")
    return r
```

The code solves the problem by iterating through each string `s` in the list `lst` and uses a generator expression to count the odd digits in each string. The count is accumulated using the `sum` function. It then constructs a string message to convey the count and appends it to the `r` list. The `enumerate` function is used to assign a unique index `i` to each string for differentiation in the output message. Finally, the `r` list is returned, containing the desired count of odd digits for each string. 

This solution is structured and concise while maintaining clarity in its approach to solving the problem and meeting the criteria for a self-contained function.