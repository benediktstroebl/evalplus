```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    elif [x for x in range(3, n+1, 2) & set([3, 5, 7])] == [x for x in range(3, n+1, 2)]:
        return 3
    elif [x for x in range(5, n+1, 2) & set([3, 5, 7])] == [x for x in range(5, n+1, 2)]:
        return 5
    elif [x for x in range(7, n+1, 2) & set([3, 5, 7])] == [x for x in range(7, n+1, 2)]:
        return 7
    else:
        return n
```