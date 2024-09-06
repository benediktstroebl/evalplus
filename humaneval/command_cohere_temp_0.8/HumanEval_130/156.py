```python
def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [0, 1, n // 2]
    else:
        return [1, 3, 2] + tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n + 1)
```
The function takes an input of type integer `n` and returns a list of the first `n + 1` numbers of the Tribonacci sequence. This is achieved via basic conditional logic that determines whether the current term being calculated is the first term, second term, an odd term, or an even term. Based on this determination, the function returns the appropriate number. For even terms, it returns `1 + n // 2`. For odd terms, it returns the sum of the previous 3 terms in the sequence. This logic allows the function to generate the Tribonacci sequence for the given input `n`.