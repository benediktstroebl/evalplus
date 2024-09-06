```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length lists, `game` and `guess`, where each element corresponds to the real result of a match and the guess for that result. It returns a list where each element is the absolute difference between the guess and the real result if they don't match, and 0 if the guess was correct. The code uses `zip` to iterate through pairs of elements in parallel, and uses an `if` statement with `abs` to calculate the distance from the guess and the ground truth.