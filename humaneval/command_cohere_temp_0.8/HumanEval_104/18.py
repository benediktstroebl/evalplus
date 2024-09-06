```python
def unique_digits(xs):
    odd = [x for x in xs if any(int(c) % 2 != 0 for c in str(x))]
    return sorted(odd)
```

The function `unique_digits` uses a list comprehension with a generator expression to filter out numbers with even digits. The condition `any(int(c) % 2 != 0 for c in str(x))` returns `True` if at least one digit of the number `x` is odd. The function then sorts the resulting list and returns it. 

To run the code, you can copy and paste it into a Python environment or script and import the `unique_digits` function. You can also modify the script to include a test suite, such as the one provided in the prompt, to verify the correctness of the solution.