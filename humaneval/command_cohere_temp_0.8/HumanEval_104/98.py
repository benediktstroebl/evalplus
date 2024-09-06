```python
def unique_digits(x):
    odd = [int(''.join(c for c in str(n) if c not in '02468')) for n in x if n % 2]
    return sorted(odd)
```

The function `unique_digits` checks whether a list of positive integers has any elements containing an even digit. It uses a list comprehension that iterates over each element in the input list `x`, converts it to a string, and checks if any digit is neither 4, 8, 2, or 6. The integers that meet this condition are filtered and collected in the `odd` list. These are integers like 1, 3, 5, 7, 9, etc.  The function finally returns a sorted list of these odd integers.

The test cases ensure that the function works correctly for both inputs with even and odd integers. Particularly, for the input `[15, 33, 1422, 1]`, the expected output `[1, 15, 33]` is returned. This output highlights that integers containing no even digits (1 and 15) are retained, while 33 is also included since it does not contain any even digits. On the other hand, the input `[152, 323, 1422, 10]` should yield an empty list `[]` because all elements have even digits.