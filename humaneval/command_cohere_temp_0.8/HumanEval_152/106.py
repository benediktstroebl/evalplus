```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length lists, `game` and `guess`, where each element corresponds to the real outcome of a match and the guessed outcome, respectively. It returns a list where each element is the absolute difference between the guess and the actual outcome if they don't match, and 0 if the guess was correct. The function uses `zip` to iterate through pairs of corresponding elements from both lists. Note that this function assumes that the input lists are of equal length and properly handles multiple wrong guesses. 

Here is an example usage of the function:
```python
game_scores = [1,2,3,4,5,1]
guess_scores = [1,2,3,4,2,-2]
print(compare(game_scores, guess_scores))
```
And this will output:
```
[0, 0, 0, 0, 3, 3]
```

Such an approach enables the comparison of guesses against known outcomes efficiently and seamlessly. It also ensures that the result is returned in the appropriate format, ready for further analysis or display. 

This code is robust and efficient, capable of handling various input scenarios and providing an accurate comparison of guessed scores against actual game outcomes.