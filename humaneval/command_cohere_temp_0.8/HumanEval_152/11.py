```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```

The Python script provides a function `compare` which takes in two arrays `game` and `guess` and returns an array of the same length denoting how far off each guess was. If they have guessed correctly, the value is 0, and if not, the value is the absolute difference between the guess and the score. The function operates by iterating through each element of both arrays through the `zip` function, comparing the values, and either assigning 0 if the guess was correct or the absolute difference between the values. 

The function works correctly as evidenced by the example usage and corresponding test cases returned:
```python
# Example usage
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
print(compare(game, guess))  # [0, 0, 0, 0, 3, 3]

# Test case
game = [0, 5, 0, 0, 0, 4]
guess = [4, 1, 1, 0, 0, -2]
print(compare(game, guess))  # [4, 4, 1, 0, 0, 6]
```