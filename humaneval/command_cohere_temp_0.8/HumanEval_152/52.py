```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length lists, `game` and `guess`, where each element corresponds to the actual outcome of a match and the predicted outcome, respectively. It returns a list where each element is the absolute difference between the guess and the actual outcome if they don't match, and 0 if the guess was correct. The code uses `zip` to iterate through pairs of corresponding elements from `game` and `guess` and uses list comprehension for aggregation.