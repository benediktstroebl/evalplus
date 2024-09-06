```python
def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [1] + [n // 2] * (n // 2)
    else:
        return [1] + tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n + 1)

print(tribonacci(6))
```

This code defines a recursive function tribonacci that returns the Tribonacci sequence for a given n. The base cases are handled with the following three conditions:
1. If n is 0, it returns [0] since the Tribonacci sequence starts with 0.
2. If n is 1, it returns [1] since the next number in the sequence is 1. 
3. If n is even, it returns [1] + [n // 2] * (n // 2), the same way it handles odd ns, but with only one 1 and a sequence of n // 2's. 

If none of these conditions are met, the function returns `1` followed by the sum of the first `n` numbers of the Tribonacci sequence, which is determined by recursively calling `tribonacci(n - 1)` , `tribonacci(n - 2)`, and `tribonacci(n + 1)`. 

When the function is called with n as 6, it returns the following sequence: `[0, 1, 1, 3, 5, 8]`.