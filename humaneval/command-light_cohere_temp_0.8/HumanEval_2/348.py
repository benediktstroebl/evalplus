```python
def truncate_number(n):
    if not n:
        return "Input should be a number"
    if not isinstance(n, (int, float)):
        return "Input should be either int or float"
    if n < 0:
        return "Input should be a positive number"
    
    s = str(n).
    return int(s[::-1]) if len(s) > 2 else s[1]
```