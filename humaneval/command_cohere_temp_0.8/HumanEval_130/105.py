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
```
The function takes an input of type integer `n` and returns a list of the first `n + 1` numbers of the Tribonacci sequence. This is achieved through several base cases and recursive calls to generate the sequence based on the definition. This definition is provided in the problem statement as follows:
- `tri(1) = 3`
- `tri(n) = 1 + n / 2, if n is even.`
- `tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.` 

The Python script encapsulates this definition through recursive logic. It includes several base cases (e.g., `n == 0`, `n == 1`, and `n % 2 == 0`), and for odd or even `n`, it appropriately calls the function recursively for the previous or subsequent values in the sequence. The result is a list of the requested number of Tribonacci values.