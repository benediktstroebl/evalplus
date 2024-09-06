```python
def unique_digits(xs):
    odd = [x for x in xs if any(int(y) % 2 for y in str(x))]
    return sorted(odd)
```

The function `unique_digits` uses a list comprehension with a generator expression to filter out numbers that have an even digit in their composition. Then the function sorts the resulting list in an ascending manner. 

The solution works thanks to the generation of expressions in Python, allowing us to iterate over all digits of a number with `int(y) % 2 for y in str(x)` and check if they are divisible by 2 with `int(y) % 2`.