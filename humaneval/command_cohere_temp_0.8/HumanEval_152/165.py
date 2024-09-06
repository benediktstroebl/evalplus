```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the score of a match, and returns an array of the same length containing the absolute difference between the guess and the score if the guess is incorrect, and 0 if the guess is correct. Here is an example:
```python
compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2])
# [0, 0, 0, 0, 3, 3]
```
This result shows the absolute difference between the guess and the score for each element of the input arrays. Correct guesses are marked with a `0`. 
The `zip` function is used to iterate through the elements of the two arrays in parallel, making it easy to calculate the absolute differences between corresponding elements.