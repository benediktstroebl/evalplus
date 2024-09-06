```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game,guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the actual outcome of a match and the guessed outcome, respectively. It returns an array of the same length containing the absolute difference between the guess and the score for each corresponding element if the guess is incorrect, and 0 if the guess is correct. 

Here is an example usage of the function:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
result = compare(game, guess)
print(result)  # Output: [0, 0, 0, 0, 3, 3]
``` 

This will return `[0, 0, 0, 0, 3, 3]`, as the guesser correctly guessed 4 outcomes and had 3 outcomes with an incorrect guess of 3 points off.