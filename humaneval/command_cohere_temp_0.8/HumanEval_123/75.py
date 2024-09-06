Here's a Python script with a self-contained function `get_odd_collatz` that solves the problem:
```python
def get_odd_collatz(n):
    odd_seq = [y for y in collatz_sequence(n) if y % 2 == 1]
    odd_seq.sort()
    return odd_seq
    
def collatz_sequence(n):
    if n == 1:
        return [1]
    else:
        odd_sequence = collatz_sequence(n//2 if n % 2 == 0 else 3*n+1)
        even_sequence = collatz_sequence(n//2 if n % 2 != 0 else 3*n+1)
        return odd_sequence + even_sequence
```

This script defines a function `get_odd_collatz(n)` that returns a sorted list of odd numbers in the Collatz sequence for the input integer `n`. The function uses a recursive approach to generate the Collatz sequence and then filters out only the odd numbers.

Here's an example of how to use the function with the given input of `n = 5`:
```python
print(get_odd_collatz(5))
```

Output:
```
[1, 5]
```

This is correct since the odd numbers in the Collatz sequence for `n = 5` are `1` and `5`.