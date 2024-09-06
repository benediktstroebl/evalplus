```python
def unique_digits(x):
    odd = [elem for elem in x if not any(int(c) % 2 == 0 for c in str(elem))]
    return sorted(odd)
```

The function `unique_digits` uses a list comprehension to filter out elements that have any even digits in their representation. The `not any()` is used to efficiently check if all digits are odd. Finally, the function returns a sorted list of these odd elements.