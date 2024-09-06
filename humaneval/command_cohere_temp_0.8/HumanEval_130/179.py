```python
def tri(n):
    result = [1, 3]
    if n > 1:
        result.extend(
            tri(x) + tri(x - 1) + tri(x + 1) for x in range(2, n + 1, 2)
        )
    result.append(n)
    return result
```

The function creates the `result` list that initially contains the first two elements of the Tribonacci sequence (`1` and `3`). If `n` is greater than 1, it iterates through all the even numbers from `2` to `n` inclusive, and for each even number it extends the `result` with the next Tribonacci number calculated using the recurrence. The `result` list is again extended with the value of `n` to finish the sequence. If `n` is only 1, the function returns a list with the first two elements of the Tribonacci sequence.