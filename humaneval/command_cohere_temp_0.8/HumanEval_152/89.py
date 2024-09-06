```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the result of a match, and returns a new array where each element represents the absolute difference between the guess and the result if the guess was incorrect, and 0 if the guess was correct. The code uses `zip` to iterate through the elements of both arrays and checks if the elements are equal (guess correct) or not (guess incorrect), and returns the corresponding value.