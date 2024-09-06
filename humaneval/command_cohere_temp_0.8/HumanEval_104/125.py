```python
def unique_digits(x):
    odd = [y for y in x if not any(int(c) % 2 == 0 for c in str(y))]
    return sorted(odd)
```

The function `unique_digits` uses a list comprehension to filter out numbers that have even digits anywhere in their decimal representation. The test examples provided in the prompt return the expected results and the function is reusable and self-contained.