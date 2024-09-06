```python
def odd_count(lst):
    r = []
    for digits in lst:
        counts = str(sum(1 for _ in range(len(digits)) if digits[_] % 2 == 1))
        r.append(f"the number of odd elements in the string {counts} of the input.")
    return r
```

This solution uses a simple loop to iterate through each string in the list and count the number of odd digits. The digit counting is done using a generator expression (`sum(1 for _ in range(len(digits)) if digits[_] % 2 == 1)`), which creates an iterable that counts the number of `True` values in the expression `digits[_] % 2 == 1`. The resulting count is then appended to the list `r` with a message describing which input string it corresponds to.