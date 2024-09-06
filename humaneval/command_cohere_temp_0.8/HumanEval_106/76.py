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
This Python script defines a function 'f' that takes an integer 'n' as input and returns a list according to the problem statement. It initially creates two lists, 'fact' and 'sum_', both with initial values set to 0 for all indices up to 'n-1'. The 'fact' list is intended to store factorials, and the 'sum_' list is for storing the sum of elements from 1 to i. The loop iterates from 1 to 'n-1' (since the base case is already set for 'i=0'). For each even 'i', it calculates the factorial of 'i' and assigns it to the 'fact' list at index 'i'. For each odd 'i', it calculates the sum of elements from 1 to 'i' and assigns it to the 'sum_' list at index 'i'. Finally, the function returns either the 'fact' list or the 'sum_' list, depending on whether 'n' is even or odd, respectively. This conforms to the example provided in the question statement.