```python
def tri(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [1] + tri(n - 1)
    else:
        return [1] + tri(n - 1) + tri(n - 2) + tri(n + 1)
```

The function takes an integer n as input and returns the list of the first n + 1 Tribonacci numbers. It checks if n is 0, returns an empty list, and if n is 1 it returns [1] respectively. In both cases, the base cases, the function does not follow the Tribonacci recurrence. Otherwise, it follows the definition of the Tribonacci sequence correctly.