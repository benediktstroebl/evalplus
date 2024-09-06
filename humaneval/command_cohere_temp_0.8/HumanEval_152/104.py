```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the actual result of a match and the predicted result by a person. It returns an array of the same length indicating how far off each guess was from the actual results, denoted by an absolute difference if the guess was incorrect or 0 if the guess was correct. 

The code uses `zip` to iterate through the elements of both arrays and checks if the elements at the current indices match by applying the `abs` function to obtain the absolute difference between the two elements, assigning it back to the corresponding element in the resulting list. If the elements match, it assigns 0 to the element. The resulting list shows how far off the guesses were regarding the actual results. 

Such a solution adheres to the problem statement and performs the necessary computations efficiently. It provides an accurate result array based on the provided `game` and `guess` arrays.