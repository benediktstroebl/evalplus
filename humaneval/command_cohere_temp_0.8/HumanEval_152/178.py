```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the score of a match, and returns an array of the same length containing the absolute difference between the guess and the score for each element, or 0 if the guess was correct. 

Here is an example usage of the function:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
print(compare(game, guess))
```
This will output:
```
[0, 0, 0, 0, 3, 3]
```
which indicates that the guesses were correct for the first 3 elements, and the guesses for the last 2 elements were 3 units off the actual scores.