```python
def odd_count(lst):
    r = []
    for digits in lst:
        count = sum(int(d) % 2 for d in digits)
        r.append(f"the number of odd elements in the string {count} of the input")
    return r
```

This code solves the problem using a list comprehension and the `sum()` function to calculate the count of odd digits in each string. The result is appended to the `r` list with the appropriate string description. The function returns the `r` list, containing the desired counts of odd digits in the input strings. 

This solution adheres to the problem statement, and should work correctly for the provided test cases. Let me know if you'd like to discuss further or explore other ideas!