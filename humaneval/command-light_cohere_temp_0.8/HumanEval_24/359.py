```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, * truth_table(n))

def truth_table(n: int) -> list[int]:
    truth_table = [0] * (n + 1)
    truth_table[0] = 1
    for i in range(1, n + 1):
        truth_table[i] = truth_table[i - 1] * i
    return truth_table

def gcd(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x
```