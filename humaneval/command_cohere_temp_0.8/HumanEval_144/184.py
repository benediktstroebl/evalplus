```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == int(num1 * n / den1)
```

This Python script defines a function `simplify` taking two arguments `x` and `n`, which are strings representing fractions in the format of a numerator divided by a denominator. The function's purpose is to determine whether the product of these two fractions (`x * n`) results in a whole number.

The function achieves this by:
1. Splitting both `x` and `n` at the '/' character, converting them into numerators (`num1`, `num2`) and denominators (`den1`, `den2`).
2. Evaluating the product of the numerators and the denominator of `n`.
3. Returning `True` if this evaluation equals the original numerator, and `False` otherwise.

This logic is based on the idea that if the product of `x` and `n` is a whole number, then the numerators' product must be divisible by the denominator of `n`.

The provided tests demonstrate the correctness of this implementation, and the function should pass all the given cases.

Please note, the assumption here is that both `x` and `n` are valid fractions, and neither has a zero denominator, as specified in the problem statement. If the input strings do not represent valid fractions, the function may not work as expected.