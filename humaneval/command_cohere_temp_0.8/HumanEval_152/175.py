```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```

The Python script provides a function `compare` which takes in two arrays `game` and `guess` and returns an array of the same length denoting how far off each guess was. If they have guessed correctly, the value is 0, and if not, the value is the absolute difference between the guess and the score. The function works by using Python's `zip` function to iterate through each element of both arrays and calculates the difference between the two values. The `abs` function ensures the difference is returned as a positive value. Finally, a list comprehension is used to create a new list that combines all the calculated differences, and the function returns this list.