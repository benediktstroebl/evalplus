```python
def fizz_buzz(n: int):
    return (n < 11 or 13) and (n < 7 or len([x for x in str(n) if x == 7])) == 0
```