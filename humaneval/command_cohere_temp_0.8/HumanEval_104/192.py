```python
def unique_digits(xs):
    odd = [x for x in xs if any(int(c) % 2 for c in str(x))]
    return sorted(odd)
```
```
The function unique_digits(xs) takes a list of positive integers called xs and uses a list comprehension to filter out integers that contain an even digit. The condition int(c) % 2 for c in str(x) checks whether each digit of the element x is odd because it returns a boolean list with the same length as the number of digits in x, and any returns True if all elements are True, indicating that the digit is odd. The function then returns a sorted list of these odd integers.
```