```python
def count_nums(arr):
    return sum(sum(map(int, str(n))) > 0 for n in arr)
```
This solution uses a powerful Python feature — `sum()` function, employed in a concise brief manner, aggregates the outcomes from a coroutine, which in turn applies a transformation to each element of the collection and judges whether the transformation output is truthy or not. Specifically, for each integer *n*, the transformation splits it into individual digits using `str(n)`, and converts each digit into an integer via `map(int, ...)`, and finally sums up these digitized integers, all in a single line, to determine whether the sum of the digits is greater than 0.