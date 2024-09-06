```python
def make_a_pile(n):
    if n == 1:
        return [n]
    else:
        return [n] + odd_even(n + 1)


def odd_even(num):
    return [x for x in range(num, num + 2, 2 if num % 2 else 1)]
```

The function `make_a_pile(n)` constructs a pile of stones with `n` levels, where the number of stones in each level is defined as follows:
- If `n` is 1, it returns a list with a single element `n` (a pile with a single stone).
- For any other value of `n` it returns a list with the first element `n` and then continues with the next odd number if `n` was odd, or the next even number if `n` was even, iterating by 2 (odd) or 1 (even) until it reaches the value of `n + 1`.

The `odd_even()` function is used within `make_a_pile()` to generate a list of even or odd numbers depending on the specification. The `range()` function with the step as an argument is used to generate the sequence of numbers, and a list comprehension is used to pack this sequence into a list.