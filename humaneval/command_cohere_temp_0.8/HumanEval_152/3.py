```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
```
This function takes two equal-length lists, `game` and `guess`, where each element corresponds to the actual result of a match and the guess for that result. It returns a list where each element is the error if the guess is wrong, or 0 if the guess is correct. This is achieved using the `zip` function to iterate through each element of both lists, taking care to handle the case where the guess is incorrect by using the `abs` function to calculate the absolute difference between the two elements.