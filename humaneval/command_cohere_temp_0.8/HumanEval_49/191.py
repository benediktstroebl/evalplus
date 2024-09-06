Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the `modp` function, which takes in two integers `n` and `p`, and returns `2` raised to the power of `n` modulo `p`. This is accomplished by using the built-in Python function `pow`, which can accept a modulus argument. 

To use this function, you can call it with any positive integer values for `n` and `p`. 

For example:
```python
print(modp(3, 5))
```
```
3
```

```python
print(modp(1101, 101))
```
```
2
```

```python
print(modp(0, 101))
```
```
1
```

```python
print(modp(3, 11))
```
```
8
```

```python
print(modp(100, 101))
```
```
1
```

This script will output the corresponding result for each test case mentioned in the original problem description.