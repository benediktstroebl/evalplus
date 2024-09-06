```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length lists, `game` and `guess`, where each element corresponds to the real result of a match and the guess for that result. It returns a list where each element is the absolute difference between the guess and the actual result if they didn't guess the result correctly, or 0 if they did guess correctly. The code uses `zip` to iterate through pairs of corresponding elements in `game` and `guess` and uses list comprehension to calculate the output list.