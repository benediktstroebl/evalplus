```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length lists, `game` and `guess`, where each element corresponds to the actual outcome of a match and the guessed outcome, respectively. It returns a list where each element is the absolute difference between the guess and the actual outcome if they don't match, and 0 if the guess was correct. The function is demonstrated in the example provided:
```python
example:
compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
``` 
The function adheres to the problem's requirement of returning a list that reflects the absolute difference between the guess and the score for each mismatch, while setting the correct guesses to 0.  This solution should work correctly for any valid input.