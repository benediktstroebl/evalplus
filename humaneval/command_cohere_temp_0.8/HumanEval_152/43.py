```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length lists, game and guess, as arguments. It returns a list of the same length, comparing each element in the two lists, and returning the absolute difference between the two elements if they don't match, and 0 if they do. This result is then returned as a list. The key process is using the zip function to iterate through the elements in parallel.