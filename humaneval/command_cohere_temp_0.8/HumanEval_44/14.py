```python
def change_base(x, base):
    return str(x) in ['0', '1'] and str(x) * base or sum([x // i for i in range(1, base + 1) if x % i == 0]) * base
```

The problem is to change the numerical base of an input number `x` to base `base`. This function achieves this by checking if the input number is a single-digit number. If it is, it returns the input number represented in the new base. Otherwise, it finds the largest digits that repeatedly divide the input number and represents them in the new base.

Here is a test case that can be used to verify the function above:
```python
def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'
    assert change_base(123, 3) == '220'
    assert change_base(123, 10) == '91'
```