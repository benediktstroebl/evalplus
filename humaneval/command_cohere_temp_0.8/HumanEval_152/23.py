```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```

The solution works by using Python's zipper to iterate over each element in `game` and `guess` simultaneously. For each pair of elements, it calculates the absolute difference between them and assigns it to the result list. If the elements are equal, it assigns 0 instead. The final result list corresponds to the return value of the function. 

The code is tested against the examples provided and should have a time complexity of O(n), where n is the length of the two arrays. 

It's worth noting that this solution assumes that the lengths of both `game` and `guess` are the same and will produce an error if they are not. Additional error handling or checking could be added for more robustness if needed.