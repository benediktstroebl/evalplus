```python
def unique_digits(x):
    odd = [elem for elem in x if not any(int(d) % 2 == 0 for d in str(elem))]
    return sorted(odd)
```
```notes
We take a list comprehension approach to filter out odd digits. Subsequently, we sort the odd-filtered list in ascending order, yielding the result. This method is both efficient and legible.```