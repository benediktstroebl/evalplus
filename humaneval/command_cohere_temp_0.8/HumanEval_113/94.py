```python
def odd_count(lst):
    r = []
    for digits in lst:
        count = 0
        for d in digits:
            if d % 2:
                count += 1
        r.append(f"the number of odd elements in the string {count} of the input")
    return r
```

This code solves the problem by iterating through each digit string in the list and counting the number of odd digits in each string. Then it replicates the string 'input' and replaces the number of odd digits in the string with the variable 'count' to fulfill the problem statement.