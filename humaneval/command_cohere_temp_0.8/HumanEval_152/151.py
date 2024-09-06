```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the actual result of a match and the predicted result respectively. It returns an array of the same length containing the absolute difference between the guess and the score for each corresponding element if the prediction is incorrect, and 0 if the prediction is correct. 

Here is an example usage of the function:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
result = compare(game, guess)
print(result)  # Output: [0, 0, 0, 0, 3, 3]
```
This will return `[0, 0, 0, 0, 3, 3]` due to the 3 elements being guessed correctly and the 4 elements being 3 units off in the given example.

This script passes the provided tests, as it satisfies the requirements of the problem statement.