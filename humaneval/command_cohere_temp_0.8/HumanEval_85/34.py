```python
def add(lst):
    even_odd = [num for i, num in enumerate(lst) if i % 2 == 1 and num % 2 == 0]
    return sum(even_odd)
```

The code uses a list comprehension to filter odd indices for even numbers and subsequently adds them using the `sum` function. The unit tests for this function would typically be based on the following examples:
```python
assert add([4, 2, 6, 7]) == 2
assert add([1, 3, 5, 7]) == 10
assert add([2, 8, 6, 4]) == 20
```