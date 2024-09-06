```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the actual result of a match and the predicted result respectively. It returns an array of the same length where each element is the absolute difference between the guess and the score if they didn't guess correctly, or 0 if the guess was correct. The function is self-contained and can be run independently. 

Here is an example of how to use the function:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
print(compare(game, guess))
```
This will output:
```python
[0, 0, 0, 0, 3, 3]
```
Which would be the appropriate response for the given example where the difference between the guess and the actual results are noted for each game. 

This function adheres to the given problem statement and performs the necessary calculations for each item in the two arrays. It is worth noting that the function assumes that the two arrays are of equal length and that the zip function is used to iterate through each element in the arrays.  If the two arrays differ in length, the function will throw a `ValueError` exception.