```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```

The function uses zip to iterate over the input arrays simultaneously, and for each pair of elements, it calculates the absolute difference between them and assigns it to the result list. If the elements are equal, it assigns 0 to the result list instead. The final result list is then returned as the output.