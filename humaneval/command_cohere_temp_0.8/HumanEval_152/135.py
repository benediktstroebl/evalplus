```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length lists, `game` and `guess`, where each element corresponds to the real outcome of a match and the guessed outcome, respectively. It returns a list where each element is either 0, if the guess was correct for the corresponding match, or the absolute difference between the guess and the actual result if it was not. This is done using the `zip` function to iterate through each element of both lists simultaneously and comparing each element.