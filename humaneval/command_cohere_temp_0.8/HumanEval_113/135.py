```python
def odd_count(lst):
    r = []
    for digits in lst:
        counts = str(len(set(digits)) - len(digits) // 2)
        r.append(f"the number of odd elements in the string {counts} of the input.")
    return r
```

This code solves the problem using a list comprehension to iterate through each string in the list and count the number of odd digits in each string. The solution leverages Python's set method, which automatically removes duplicate digits, and the len function to determine the count of odd digits. Finally, the result is formatted as a string to complete the problem statement.