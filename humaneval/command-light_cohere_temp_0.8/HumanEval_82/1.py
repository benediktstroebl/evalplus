```python
def prime_length(string):
    if len(string) <= 1:
        return False
    s = set(string)
    for i in range(2, len(s) + 1):
        if s.isub(i):
            return False
    return True
```