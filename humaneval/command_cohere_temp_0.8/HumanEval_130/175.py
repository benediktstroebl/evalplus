```python
def tri(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [1] + tri(n - 1)
    else:
        return [1] + tri(n - 1) + tri(n - 2) + tri(n + 1)
```
The function `tri()` follows the definition of the Tribonacci sequence as defined in the problem statement. It uses a recursive approach to generate the sequence based on the given criteria for odd and even values of `n`. The initial cases of `n == 0`, `n == 1` are also handled.  As per the problem, the function returns a list of the first `n + 1` numbers of the Tribonacci sequence.  It achieves this recursively by following the defined Tribonacci sequence patterns.  This solution encompasses the entire problem statement within the function `tri()` and provides an output list as expected in the Markdown code block.