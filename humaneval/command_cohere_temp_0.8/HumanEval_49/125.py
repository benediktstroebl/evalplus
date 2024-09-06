```python
def modp(n, p):
    return (1 << n) % p
```

This function takes two inputs, `n` and `p`, and returns the result of multiplying 2 by itself `n` times and then taking the remainder when divided by `p`. This operation is performed using the `<<` operator, which performs bitwise left shift, and the `%` operator, which returns the remainder of a division operation.

Here's an example usage of the function:
```python
print(modp(3, 5))
print(modp(1101, 101))
print(modp(0, 101))
print(modp(3, 11))
print(modp(100, 101))
```

This will output:
```
3
2
1
8
1
```

This demonstrates the function working correctly for the provided test cases, outputting the expected values based on the specification given in the code block. 

Please let me know if this resolves the problem you were facing or if you need further assistance! Feel free to provide more details or additional code blocks if you want assistance with a different problem or with more complex scenarios.