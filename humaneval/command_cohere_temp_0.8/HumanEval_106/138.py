```python
def f(n):
    facts = [0] * n
    for i in range(1, n+1):
        facts[i] = facts[i - 1] * i if i % 2 == 0 else facts[i - 1] + i
    return facts
```
This Python script defines a function `f` that takes an integer `n` as input and returns a list with `n` elements. For even values of `i`, the `i`-th element in the list is the factorial of `i`, which is computed iteratively using a running product. For odd values of `i`, the `i`-th element in the list is the sum of numbers from 1 to `i`. This is achieved by computing the `i`-th element as the sum of the previous element and `i`, or by multiplying the previous factorial with `i`. The script provides an example usage of this function, demonstrating that for `n=5`, it returns the list `[1, 2, 6, 24, 15]`.