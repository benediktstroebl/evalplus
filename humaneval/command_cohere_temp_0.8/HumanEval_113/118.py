```python
def odd_count(lst):
    r = []
    for digits in lst:
        counts = str(len(set(digits)) - len(digits) // 2)
        r.append(f"the number of odd elements in the string {counts} of the input.")
    return r
```

This code solves the problem using a list comprehension to filter out odd and even digits and calculate the count of odd digits in each string in the list. Finally, it creates a list of strings describing each string's odd digit count.