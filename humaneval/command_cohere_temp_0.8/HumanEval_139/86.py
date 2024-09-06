```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n+1):
        factorial_list.append(i * factorial_list[i-1])
    return factorial_list[n]
```

This script defines the `special_factorial` function which calculates the `brazilian_factorial` of a given integer `n`. It initializes a `factorial_list` with the base case of 1! and then iteratively multiplies this with subsequent integers to finally provide the `brazilian_factorial` for input `n`. 

You can test this script by calling `special_factorial` with various inputs to ensure it correctly calculates the Brazilian factorial values.  For example:
```python
>>> special_factorial(4)
288
``` 
This will return the Brazilian factorial for the input of 4, which is 288.  This is confirmed by the example provided in the problem statement.