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

This code solves the problem by taking an list of list of digits and creating a list of corresponding string messages. Each message describes the number of odd digits in the corresponding list of digits.