```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == int(num1 * n / den1)
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. The function first splits each string into two integers using the `split()` method and converts them into integers using the `map()` function. Then, it checks if `num1 * den2` is equal to `int(num1 * n / den1)`. If they are equal, it returns `True`, otherwise, it returns `False`.

Here is a test drive for the script:
```python
# Test drive
assert simplify("1/5", "5/1") == True
assert simplify("1/6", "2/1") == False
assert simplify("7/10", "10/2") == False
```

The tests assert that the function `simplify()` returns the expected values based on the problem statement. 

The solution relies on the assumption that the denominator of the multiplier `n` is non-zero, as division by zero would raise an exception. Feel free to let me know if you'd like me to explain any of the steps outlined in the solution or provide additional code explanations!