```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It returns a list where each element represents the difference between the corresponding elements in the `game` and `guess` arrays, or 0 if the guess was correct. The function is designed to compare the expected game results (`game`) with the user's guesses (`guess`), returning a list that indicates how far off each guess was from the actual result. 
The examples provided in the prompt yield the following results:
- `compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]`
- `compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]`
The resulting lists show how far off each guess was from the corresponding game result. For example, the second example returns `4` at the second index, indicating that the guess of `1` was `4` off from the actual result `5` in the corresponding game result. PLease note that the code assumes that the lengths of both arrays are identical and that the assumption of pairing up elements might lead to unexpected results if the arrays are not of the same length.