```python
def fizz_buzz(n: int):
    return len({i for i in range(1, n+1) if i % 10 == 7 and i % 13 == 0})

# Test the function with inputs 50, 78, and 79
print(fizz_buzz(50)) == 0
print(fizz_buzz(78)) == 2
print(fizz_buzz(79)) == 3)
```