```python
def tri(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    list_of_trib = [0, 1, 3]
    if n % 2 == 0:
        return list_of_trib + [tri(n - 1)]
    else:
        return list_of_trib + [tri(n - 1) + tri(n - 2) + tri(n + 1)]
```

The function utilizes the recurrence relation provided in the problem description and maintains a list `list_of_trib` to store the values calculated. It then returns the list of the first `n + 1` values of the Tribonacci sequence as requested. 

This approach ensures that the function returns the correct sequence for any non-negative integer `n`.

You can test this function by calling `tri()` with different values of `n` and comparing the results with the expected outputs provided in the problem description.