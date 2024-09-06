```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the actual outcome of a match and the guessed outcome by the person, respectively. It returns an array of the same length indicating how far off each guess was from the actual outcome, either 0 if the guess was correct or the absolute difference between the guess and the actual outcome if not. 

Here is an example usage of the function:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
result = compare(game, guess)
print(result)  # Output: [0, 0, 0, 0, 3, 3]
``` 

This will return `[0, 0, 0, 0, 3, 3]`, as the guesser correctly guessed 4 outcomes and was off by 3 for the two mismatches.