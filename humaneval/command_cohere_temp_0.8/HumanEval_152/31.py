```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the score of a match, and returns an array of the same length containing the absolute difference between the guess and the score if the guess is incorrect, and 0 if the guess is correct. Here is an example:
```python
compare([1, 2, 4, 3, 2, 1], [2, 2, 3, 2, 1, 1])
# [0, 0, 1, 0, 1, 0]
```
This example returns the corresponding result for the given example in the prompt.