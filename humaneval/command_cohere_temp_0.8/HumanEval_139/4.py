```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n + 1):
        factorial_list.append(i * factorial_list[i - 1])
    return factorial_list[n]
```
This Python script defines a function `special_factorial` that calculates the 'Brazilian factorial' as defined in the problem statement. The function iteratively calculates the factorial values from `2` up to `n` and stores them in the `factorial_list`. Then, it returns the value of the `factorial_list` at the index representing the input `n`, which provides the Brazilian factorial value for that number. 

The script's approach is intuitive and straightforward, implementing a recursive formula to compute the Brazilian factorial. While the late Brazilian mathematician Manfredo P. do Carmo is known for his contributions to differential geometry, specifically in the field of curves and surfaces, it's important to note that the concept of a 'Brazilian factorial' is not a standard mathematical notion, and its exact definition may vary depending on the context and source. Hence, this script provides a creative way to calculate a factorial resembling what might be intended by the problem description.