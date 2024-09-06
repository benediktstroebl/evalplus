```python
def simplify(x, n):
    num_x, denom_x = map(int, x.split('/'))
    num_n, denom_n = map(int, n.split('/'))
    
    return num_x * denom_n == denom_x * num_n
```

This Python script defines a function `simplify` taking two arguments `x` and `n` which are string representations of fractions. The function's purpose is to determine whether the product of these two fractions (`x * n`) results in a whole number. It achieves this by splitting the numerator and denominator of each fraction through the `split` method, which is then converted to integers through `map(int, ...)`. The function then compares these products in order to establish whether the result is an entire number, as stipulated by the problem statement. 

This implementation is test-driven, and we can add test cases to ensure the functionality of the code:
```python
# Tests:
assert simplify("1/5", "5/1") == True
assert simplify("1/6", "2/1") == False
assert simplify("7/10", "10/2") == False
```