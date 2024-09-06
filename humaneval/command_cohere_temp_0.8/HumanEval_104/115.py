```python
def unique_digits(x):
    odd = [int(''.join(c for c in str(i) if c not in '02468')) for i in x if i % 2 != 0]
    return sorted(odd)
```
```
The function unique_digits processes each number in the list x as follows:
1. Int(): Converts the number to an integer, which allows us to perform mathematical operations on it.
2. '.join(c for c in str(i) if c not in "02468")': Converts the integer to a string, but instead of using the standard str() function, it uses a list comprehension. This list comprehension selects only the odd digits ('1', '3', '5', '7', and '9') from the string representation of the number.
3. Finally, it stores the filtered numbers in the list odd.

Once all numbers in the list x are processed, the function returns the sorted odd list.
```