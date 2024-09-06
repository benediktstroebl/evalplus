```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        tens, remainder = divmod(n, 10)
        if remainder == 0: 
            return str(tens) + "x"
        elif remainder == 5: 
            return str(tens) + "l"
        else: 
            return str(tens) + str(remainder)
```