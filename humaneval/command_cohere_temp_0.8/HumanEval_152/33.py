```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the actual result of a match and the predicted result respectively. It returns an array of the same length where each element is the absolute difference between the guess and the score if they didn't guess correctly, and 0 if the guess was correct. 

Here is an example usage of the function:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
result = compare(game, guess)
print(result) 
 ```
This code will print the following output:
```python
[0, 0, 0, 0, 3, 3]
```

The function can also be simplified further using Python's `pandas` library, which provides a `diff` function that returns the difference between two arrays:
```python
import pandas as pd

def compare(game, guess):
    return pd.Series(guess) - pd.Series(game)
```
In this version, the function treats the arrays as pandas Series and simply subtracts one from the other.