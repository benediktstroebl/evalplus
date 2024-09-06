```python
def unique_digits(x):
    odd = [int(''.join(c for c in str(i) if c % 2 != 0)) for i in x if int(''.join(c for c in str(i) if c % 2 != 0)) <= int('9'*len(str(i)))]
    return sorted(odd)
```

The algorithm for this solution is:
1. For each number in the input list, we check whether it is possible to create it using odd digits only.
2. We use the `str(i)` function to convert the integer to a string and `c for c in str(i)` to create an iterator over its digits.
3. We use a list comprehension and the `join()` method to convert the iterator of digits to a string.
4. We use `c % 2 != 0` to select only the odd digits.
5. We use int() to convert the string of odd digits back to an integer.
6. If the integer (created from odd digits) is less than or equal to the maximum integer that can be created from the same number of odd digits (i.e. '9'*len(str(i))), then the number contains only odd digits.
7. Finally, we return the list of all integers that can be represented with only odd digits, sorted in increasing order.