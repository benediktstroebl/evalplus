```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
```
This function takes two equal-length lists, `game` and `guess`, where each element corresponds to the real outcome of a match and the guessed outcome, respectively. It returns a list where each element is the absolute difference between the guess and the actual result if they don't match, and 0 if the guess was correct. The code uses `zip` to iterate through pairs of elements in parallel, simplifying the logic required to compare each element and reducing the amount of code required.