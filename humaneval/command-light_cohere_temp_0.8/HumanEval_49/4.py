```python
def modp(n, p):
    if p == 0:
        return 1
    return (pow(n, p-2, p) % p)

# Test case
print(modp(1101, 101))  # Output: 2
```