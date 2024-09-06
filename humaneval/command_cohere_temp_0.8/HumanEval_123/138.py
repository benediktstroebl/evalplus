```python
def get_odd_collatz(n):
    odd_collatz = [3*i+1 for i in range(1, n+1, 2)] + [i for i in range(3, n+1, 2) if i%2]
    return odd_collatz
```

This function uses two separate list comprehensions to generate the odd numbers in the Collatz sequence. The first comprehension considers the odd numbers at the beginning of the sequence, which are of the form 3*i+1, where i is incremented by 2 to skip even numbers. The second comprehension considers the odd numbers after the first batch, which are of the form i where i increases by 2 and is odd. These two comprehensions are then combined to give the odd numbers in the Collatz sequence for n. The result is then returned as a list. 

This should provide a solution to the problem statement given a positive integer n. Let me know if you would like any adjustments made to the code!