```python
def odd_count(lst):
    r = []
    for digits in lst:
        count = sum(1 for digit in digits if digit % 2 != 0)
        r.append(f"the number of odd elements in the string {count} of the input")
    return r
```

This script defines a function `odd_count` which takes a list of lists, where each inner list consists of digits. It calculates the number of odd digits in each inner list and returns a list of strings describing these counts, as specified in the problem statement. The `sum` function is used within a loop to calculate the count of odd digits in each list of digits.