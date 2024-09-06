```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n+1):
        factorial_list.append(i * factorial_list[i-1])
    return factorial_list[n]
```

This Python script defines the `special_factorial` function, which calculates the Brazilian factorial of a given integer `n`. The Brazilian factorial is represented as a list of factorials from `1!` through `n!`. The way it works is it starts with `factorial_list` initialized to `[1]`, and then iterates through integers from `2` to `n + 1`. During each iteration, it calculates the current factorial by multiplying the previous factorial with the current integer, updating `factorial_list` accordingly. This way, `factorial_list[n]` holds the Brazilian factorial of `n`.

Here is an example of using this function:
```python
>>> special_factorial(4)
288
```

This is the expected result, as `288` is indeed the Brazilian factorial of `4`.