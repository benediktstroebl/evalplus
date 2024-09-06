```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It compares the elements of these arrays, which represent game scores and user guesses respectively, pairwise using `zip`. For each pair of elements, it calculates the absolute difference (`abs`) between them, assuming they are not equal. If the elements match, it assigns a value of 0 to indicate a correct guess. These differences or zeroes are then aggregated into a single array `result`. The function returns this resulting array, where each element represents how far off the corresponding guess was from the actual score. 

The fundamental idea is to loop through each element of both arrays and for each element subtract the guess from the game result and assign the absolute difference to the result list. If the guess and the game result are the same then the difference is 0 and this value is also added to the result list. The function returns the resulting list.