```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
```
This function takes two equal-length lists, `game` and `guess`, where each element corresponds to the real result of a match and the guessed result. It returns a list where each element is the absolute difference between the two lists, if the guess is wrong, or 0 if the guess is correct. The code uses `zip()` to iterate through the elements of both lists simultaneously, and the `abs()` and list comprehensions do the rest.