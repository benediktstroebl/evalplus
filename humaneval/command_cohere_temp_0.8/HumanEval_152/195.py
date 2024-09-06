```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length lists, `game` and `guess`, where each element corresponds to the actual outcome of a match and the predicted outcome, respectively. It returns a list where each element is either 0, if the guess was correct for the corresponding match, or the absolute difference between the guess and the actual outcome if it was not. This result is produced by iterating through each element of both lists through the `zip` function, calculating the absolute difference (`abs`), and either storing the result or 0 in a list, which is returned at the end. 
The behavior of the code is illustrated in the following example:
```python
print(compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2,-2]))
```
The output will be:
```
[0, 0, 0, 0, 3, 3]
```
as each element not equal to -2 in the guess list is correctly guessed, whereas the absolute difference between -2 and the respective outcome is returned for that entry. Gives an output as in the example in the prompt.  Any other list of equal length could be passed in place of `game` and `guess` to achieve the same result, as the function is designed to be self-contained.