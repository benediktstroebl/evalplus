```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game,guess)]
```
This function takes two equal-length lists, `game` and `guess`, as input and returns a list of the same length, where each element represents how far off each guess was from the corresponding game result, or 0 if the guess was correct. This is achieved using the `zip` function to iterate through each element of both lists simultaneously and compare the elements. Note that this function assumes that the input lists are of the same length and that the indices correspond to each other.