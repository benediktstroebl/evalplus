```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, x)
 
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# run the function and print the result
n = 15
result = largest_divisor(n)
print(result) # 5
```