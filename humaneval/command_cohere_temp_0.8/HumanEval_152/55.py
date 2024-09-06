```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the result of a match, and returns an array of the same length showing how far off each guess was. Correct guesses return a value of 0, and incorrect guesses return the absolute difference between the guess and the actual result. The code uses `zip` to iterate through the elements of both arrays to compare corresponding elements efficiently. 

Here is a brief explanation of the correctness of the solution:
- To solve this problem, we need to compare each element in the `game` array with the corresponding element in the `guess` array.
- We do this by using `zip`, which combines each element of both arrays in pairs, and then iterating through this combined iterable with a list comprehension.
- For each pair of elements `(x, y)`, we check if `x` and `y` are equal. If they are, we return 0 as the corresponding guess was correct. If they are not, we return the absolute difference `abs(x-y)` to indicate how far off the guess was from the actual result.
- Finally, we list comprehensions return the resulting array of comparisons.