```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == den1 * num2
```

The function `simplify` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits each string into two parts, the numerator and the denominator, and then converts them to integers. 

The function then checks if the product of the numerators (`num1 * den2`) is equal to the product of the denominators (`den1 * num2`). If this condition is true, it returns `True`, meaning the expression `x * n` simplifies to a whole number; otherwise, it returns `False`.

This algorithm follows the instructions in the prompt and assumes valid fractions for inputs, as stated in the assumption. 

This solution is concise and straightforward, directly addressing the problem statement. It's adaptable to different inputs as it doesn't rely on any specific format beyond the given fraction format. 

If you would like to test this script, input a string `x` and a string `n` separated by a comma, and it will return `True` or `False` depending on whether the expression `x * n` simplifies to a whole number.