```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length lists, `game` and `guess`, where each element corresponds to the real results of the matches and the guessed results by the person, respectively. It returns a list where each element is the absolute difference between the guess and the real result of the match if they didn't guess correctly, or 0 if the guess was correct. The code uses `zip` to iterate through pairs of corresponding elements in both lists. And uses `abs` to calculate the absolute difference between the elements, additionally subtracting the minimum of two values if they are equal to avoid unnecessary calculations.