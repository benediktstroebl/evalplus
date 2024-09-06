```python
def odd_count(lst):
    r = []
    for num in lst:
        count = 0
        for c in num:
            if c % 2:
                count += 1
        r.append(f"the number of odd elements in the string {count} of the input")
    return r
```

This code solves the problem by using two nested loops. The outer loop iterates through each string in the list, and the inner loop iterates through each digit in the current string to count the number of odd digits. The total count is then appended to the answer list, which is returned at the end. This solution is concise and efficient, correctly solving the problem statement.