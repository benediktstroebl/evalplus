```python
def truncate_number(n):
    # integer part calculation
    x = int(n)
    return x if x > n else x - n 

# tests 
assert truncate_number(3.5) == 0.0
assert truncate_number('0.5') == 0.0
assert truncate_number(-3.5) == -0.0
assert truncate_number(0.0) == 0.0
assert truncate_number('3.2') == 0.0
assert truncate_number('03.99') == 0.0
assert truncate_number(1e1223) == 12200

```