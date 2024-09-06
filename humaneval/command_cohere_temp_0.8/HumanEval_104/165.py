```python
def unique_digits(x):
    odd = [int(''.join(c for c in s if c % 2 != 0)) for s in x]
    return sorted(odd)
```
```
The function unique_digits processes the list of integers x as follows:
- It iterates through every element s in x and creates a new list containing the odd digits only, using the expression c for c in s if c % 2 != 0. This generates a list of integers in the same order as the digits in s.
- The list of odd digits is then converted to integers using the int() function and stored in the list odd.
- Finally, the function returns a sorted version of the list odd, achieving the desired result of sorting the list in ascending order.
```