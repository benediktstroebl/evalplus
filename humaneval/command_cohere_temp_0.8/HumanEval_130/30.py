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
The function takes an input of type integer and returns a list of the first n + 1 numbers of the Tribonacci sequence. We can divide the logic into three branches, tri(1) = 3, tri(n) = 1 + n / 2 if n is even, and, tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1) if n is odd. We can initialize the list to be returned based on these cases and incorporate the recursive calls accordingly.