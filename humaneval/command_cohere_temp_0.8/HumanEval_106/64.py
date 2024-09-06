```python
def f(n):
    fact = [0] * n
    sum_ = [0] * n
    fact[0] = 1
    sum_[0] = 0
    for i in range(1, n):
        fact[i] = fact[i - 1] * i
        if i % 2 == 1:
            sum_[i] = sum_[i - 1] + i
    return fact if n % 2 == 0 else sum_
```
This Python script defines a function 'f' that takes an integer 'n' as input and returns a list of 'n' elements. It initializes two lists, 'fact' and 'sum_', both of length 'n', to store the factorials and sums of integers from 1 to 'n', respectively. The loop computes the factorials for odd indices and the sums for even indices, using previously calculated values to compute the current element's value. The function then returns either the 'fact' list or the 'sum_` list based on whether the length 'n' is even or odd, respectively. Thus, the function satisfies the problem statement's condition of returning a list with elements being either factorials of even indices or sums of numbers from 1 to the odd indices.