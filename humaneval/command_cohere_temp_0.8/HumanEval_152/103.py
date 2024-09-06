```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the actual result of a match and the predicted result by a person. It returns an array of the same length indicating how far off each guess was from the actual results, categorized by the following rules:
1. If a person's guess matches the actual result, it returns `0`. 
2. If not, it returns the absolute difference between the guess and the actual outcome.

Here is an example usage of the code for clarification:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
print(compare(game, guess))
# Output: [0, 0, 0, 0, 3, 3]
``` 

The output returns the array of exactly `0` values for the elements where the guesses correctly predicted the outcomes, and non-zero values for the elements where the prediction was incorrect. 

Another example is:
```python
game = [0, 5, 0, 0, 0, 4]
guess = [4, 1, 1, 0, 0, -2]
print(compare(game, guess))
# Output: [4, 4, 1, 0, 0, 6]
``` 

In this example, the person's guesses were not all correct, resulting in non-zero values in the output array. 

The code uses `zip` to iterate over the elements of both arrays at the same time, and uses Python's tuple unpacking with the `if` statement to determine whether the elements match.