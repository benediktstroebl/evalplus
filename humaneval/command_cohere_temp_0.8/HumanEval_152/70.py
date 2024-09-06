```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
```
This function takes two equal-length lists, game and guess, as input. It returns a list where each element is the absolute difference between the corresponding elements in game and guess if they don't match, or 0 if the guess was correct. The result is a list showing how far off each guess was.