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
This Python script defines a function 'tri()' that computes the Tribonacci sequence, a variation of the Fibonacci sequence. It handles the base cases (n=0, n=1) by returning an empty list and a list with 1 respectively. In the case of an even n, it iterates one step, adding 1 to the result. In the case of an odd n, it iterates 2 steps, adding 1 to the result and appending the sum of the previous two steps.