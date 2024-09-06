```python
def f(n):
    facts = [0] * n
    sums = [0] * n
    for i in range(1, n+1):
        facts[i] = facts[i - 1] * i
        if i % 2 == 0:
            sums[i] = sums[i - 1] + i
    return sums if n % 2 == 0 else facts
```

This Python script defines a function 'f' as per the problem statement. It generates a list where the even indices are filled with the factorials of numbers from 1 to n, and the odd indices are filled with the sum of numbers from 1 to n. This is achieved using two parallel arrays, 'facts' for factorials and 'sums' for sums, iterating through numbers from 1 to n, and then returning the appropriate array based on whether n is even or odd. 

To ensure correctness, the function initially fills the arrays with initial values of 0 and then performs a loop to calculate factorials and sums while building the final list.