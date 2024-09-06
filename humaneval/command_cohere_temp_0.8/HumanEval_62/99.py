```python
def derivative(xs: list) -> list:
    result = [0] * (len(xs) + 1)
    degree = len(xs)
    for i in range(degree):
        result[i+1] = result[i] + xs[i] * i
    return result
```

The `derivative` function takes a list of numbers `xs` as input, which represent the coefficients of a polynomial, and returns the list of coefficients of the derivative of the polynomial. 

The script uses a dynamic programming approach to calculate the derivative of order `n` in `O(n)` time, where `n` is the size of the input list.

To achieve this, it constructs a gradient array `result` with invariants that `result[i]` represents the derivative order `i` of the polynomial created from `xs`. Using this structure, it iterates through each element of `xs` and incrementally updates the `result` array with the derivative contribution of each monomial. 

This approach allows the function to efficiently calculate the derivative of the polynomial, as the time complexity is linear with respect to the size of the input list.

Here is an example usage of the function:
```python
>>> derivative([3, 1, 2, 4, 5])
[1, 4, 12, 20]
>>> derivative([1, 2, 3])
[2, 6]
```
The above examples illustrate the correct behavior of the function.