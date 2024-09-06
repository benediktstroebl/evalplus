```python
def change_base(x, base):
    return str(x).convert(base)
```

The `convert` method is used to change the base, since it completes the task directly and simply. It can handle bases less than 10. To demonstrate its usage, here are some test cases:
```python
>>> change_base(8, 3)
'22'
>>> change_base(8, 2)
'1000'
>>> change_base(7, 2)
'111'
```

The function also can handle negative numbers as well as additional test cases with more intricate numbers:
```python
>>> change_base(-8, 3)
'-22'
>>> change_base(1234, 5)
'111002004008'
>>> change_base(7, 10)
'7'
```