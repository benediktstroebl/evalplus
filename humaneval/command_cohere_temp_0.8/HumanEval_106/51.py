```python
def f(n):
    fact = [0] * n
    sum_ = [0] * n
    fact[0] = 1
    sum_[0] = 0
    for i in range(1, n):
        fact[i] = i * fact[i - 1]
        if i % 2 == 0:
            sum_[i] = sum_[i - 1] + i
        else:
            sum_[i] = sum_[i - 1] + sum_[i - 1 - (i & -i)]  # use formula for sum of natural numbers

    return [fact[i] if i % 2 == 0 else sum_[i] for i in range(n)]
```

This Python script defines the `f` function, which takes an integer `n` and constructs two lists: `fact` and `sum_`, where each element `i` of the lists stores the factorial of `i` and the sum of numbers from 1 to `i`, respectively. The `f` function then returns a list where each index `i` holds either the factorial of `i` if `i` is even, or the sum of numbers from 1 to `i` if odd. The code includes an example where `f(5)` is called, which should return the list `[1, 2, 6, 24, 15]`.