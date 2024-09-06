```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length lists, `game` and `guess`, as arguments. It returns a list where each element corresponds to the result of the comparison between the respective elements of `game` and `guess`. 

The purpose of the function is to determine how close each guess was to the actual results of the games, expressed as scores in `game`. It does this by computing the absolute difference between the guess and the score, for each element in the respective lists.

If a guess matches the score, the function returns `0` for that element, expressing that the user's guess was correct for that particular game or match. 

This solution complies with the Test Cases provided, correctly returning the resulting list of differences between guesses and scores. 
For example, in one of the Test Cases, the function is called as follows:
```python
compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2])
```
The output of this call will be: `[0, 0, 0, 0, 3, 3]`. 

This is correct, as in the respective indices:
- The guess `1` matched the score `1`, returning `0`.
- The guess `2` did not match the score `3`, returning the absolute difference, `3`.
- The guess `4` was correct, returning `0`. 
- The guess `2` did not match the score `5`, returning `3`. 

The function also handles additional edge cases, correctly computing the differences or returning `0` when the guess is correct. Hovewer, user is advised to test this function with more complex inputs, being always cautious with the types of inputs lists, and the consistency of the lengths of both lists.