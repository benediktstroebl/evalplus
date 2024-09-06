```python
def search(lst):
    freq, max_val = -1, 0
    for i in lst:
        if i > 0:
            freq = lst.count(i)
            if freq >= i and (max_val < 0 or i > max_val):
                max_val = i
    return max_val if max_val > 0 else -1
```

This script defines a function 'search' which iterates through the list 'lst' and examines each positive integer. It calculates the frequency of each integer and compares it to the integer's value itself. If the frequency is greater than or equal to the integer's value and it's greater than the previously recorded maximum value, it updates the maximum value and frequency. Finally, it returns the maximum value found if it's greater than zero, or -1 if no such integer is found. 

The following test cases illustrate the function's behavior:
```python
test_cases = [
    ([4, 1, 2, 2, 3, 1], 2),
    ([1, 2, 2, 3, 3, 3, 4, 4, 4], 3),
    ([5, 5, 4, 4, 4], -1)
]

for lst, expected in test_cases:
    assert search(lst) == expected
```

The expected output is:
```bash
2
3
-1
```

The script successfully identifies the greatest integer satisfying the given criteria in each case, returning the correct values of 2, 3, and -1 respectively.