```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```
This Python script provides a function that takes two lists, namely `game` and `guess`, where the former represents the sequence of match scores and the latter represents guesses respectively. The function proceeds to calculate the absolute difference between each pair of corresponding elements, storing the results in a new list named `result`. Notably, if a guess matches the corresponding score, the function assigns a value of 0 to that element in the `result` list. The final list `result` signifies the degree of deviation from the correct scores for each respective guess, where each element assumes the absolute difference between the guess and the score, unless the guess was correct, in which case it assigns 0.