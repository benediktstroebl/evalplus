```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This Python script defines a function named `compare` which takes two arrays, `game` and `guess`, as input. It compares the elements of the two arrays pairwise using `zip`, and for each pair, it calculates the absolute difference between the two elements if they are different, indicating that the guess was incorrect. If the elements are the same, it returns 0 to indicate a correct guess. The results are then aggregated to produce an array that reflects how far off each guess was, with correct guesses marked as 0 and incorrect guesses preceded by the absolute difference. 

Here's an example usage of the function:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
result = compare(game, guess)
print(result)  # Output: [0, 0, 0, 0, 3, 3]
``` 
And another example:
```python
game = [0, 5, 0, 0, 0, 4]
guess = [4, 1, 1, 0, 0, -2]
result = compare(game, guess)
print(result)  # Output: [4, 4, 1, 0, 0, 6]
``` 
The function's behavior is consistent with the problem statement provided, and the examples demonstrate how it handles various scenarios of correct and incorrect guesses. 

This script efficiently computes and returns the desired array of results, providing insight into how well the guesses aligned with the actual outcomes.