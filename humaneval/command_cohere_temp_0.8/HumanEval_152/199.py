```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the actual result of a match and the predicted result respectively. It returns an array of the same length indicating how far off each guess was. If the guess was correct, it returns 0, otherwise it returns the absolute difference between the guess and the actual result. 

Here is an example use case:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
print(compare(game, guess))
```
This will output:
```
[0, 0, 0, 0, 3, 3]
```
Which indicates that the guesses for the first 4 matches were all correct, and the returns values for the last two matches are 3 and 3, indicating the difference between the guess and the actual results of -3 and 7 respectively. 

The `zip` function enables the function to iterate through the elements of both arrays in parallel, making it possible to compare each element in the arrays sequentially. The `abs` function is used to calculate the absolute difference between the guess and the game, for the cases where the guess was not correct.