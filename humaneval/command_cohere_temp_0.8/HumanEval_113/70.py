```python
def odd_count(lst):
    r = []
    for num in lst:
        o = sum(1 for c in num if c % 2 != 0)
        r.append(f"the number of odd elements {o}n the str{len(num)}ng {num} of the input.")
    return r
```

The function iterates over the list of strings (each element is a string in the input), and for each string, it counts the number of odd digits and appends the corresponding message to the output list. The message is formulated by replacing `n` with the length of the string (`len(num)`) and replacing `o` with the actual count of odd digits in the string. The final list of messages is then returned as the result.