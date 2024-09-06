```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` takes two integers 'n' and 'p' as input, and returns `2^n modulo p` using the `pow()` function. This solution is concise and straightforward, letting the built-in `pow()` function do the heavy numerical lifting. 

This approach is both elegant and efficient, and it handles all edge cases, including `n == 0`, `p == 1`, and various numeric scenarios. 

To clarify a few test cases provided in the markdown code block, here are some examples of the function's behavior:
```python
>>> modp(3, 5)
3
>>> modp(1101, 101)
2
>>> modp(0, 101)
1
>>> modp(3, 11)
8
>>> modp(100, 101)
1
```

This demonstrates that the function correctly returns the modulo-ed result for various cases. 

Note that the `pow()` function returns an integer, and therefore, there is no need to worry about decimal points or floating-point errors in this context. 

If you wanted to achieve the same result with floating-point numbers, you could use the `math` module, like so: 

```python
import math

def modp(n, p):
    return math.pow(2, n, p)
``` 

But floating-point numbers are not necessary for the problem, and the integer-based solution is both accurate and efficient.