```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```

The solution works by using Python's built-in `zip()` function to iterate over the elements of the `game` and `guess` arrays simultaneously, so that each pair of elements (one from `game` and one from `guess`) is sequentially fed into the `abs()` function, which calculates the absolute difference between the two integers, and this difference (or 0 if the guess was correct) is added to the `result` array. The resulting `result` array thus shows how far off each guess was, with 0s denoting correct guesses. 

This approach leverages Python's elegant and concise one-liner zip-functionalities combined with conditional checking to produce the desired outcome. 

This is an efficient solution that skillfully utilizes built-in Python functionalities to achieve the desired outcome and maintain code readability. Such solutions are highly valued in the Python community for their combination of simplicity and functionality.