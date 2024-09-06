```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the score of a match, and returns an array of the same length containing the absolute difference between the guess and the score if the guess is incorrect, and 0 if the guess is correct. Here is an example:
```python
compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2])
# [0, 0, 0, 0, 3, 3]
``` 

This approach follows the instructions provided in the markdown code block. It returns an array that shows how far off each guess was, with 0 indicating a correct guess and a non-zero value showing the absolute difference between the guess and the score otherwise. 

The tests are not included as you requested a self-contained script, but the function above should pass the tests provided in the markdown code block.  If you wish to include those tests, I can provide a simple test harness for evaluation.