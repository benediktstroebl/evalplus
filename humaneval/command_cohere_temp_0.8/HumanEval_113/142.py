```python
def odd_count(lst):
    r = []
    for digits in lst:
        count = sum(1 for d in digits if d % 2 == 1)
        r += [f"the number of odd elements in the string {count} of the input"]
    return r
```

This script defines a function `odd_count` which takes in a list of lists, where each inner list consists of digits. It iterates through each list of digits, counting the number of odd digits using a generator expression. Then, it constructs a string containing the corresponding message and odd digit count, adding each one to the `r` list. The final output is the list `r`, which contains the desired strings.