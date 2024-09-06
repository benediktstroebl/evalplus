```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
```
This function takes two equal-length lists, `game` and `guess`, where each element corresponds to a match result. It returns an list where each element is the absolute difference between the guess and the score if they didn't guess the result correctly, and 0 if they did guess correctly. 

Here is an example usage of the function:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
print(compare(game, guess))  # output: [0, 0, 0, 0, 3, 3]
``` 

The example depicts a successful match prediction, as the resultant list consists of all '0's. 

Here is another example to demonstrate the use of the function for a case with prediction failures:
```python
game = [0, 5, 0, 0, 0, 4]
guess = [4, 1, 1, 0, 0, -2]
print(compare(game, guess))  # output: [4, 4, 1, 0, 0, 6]
``` 

The output in this example shows the list with the relevant errors for each incorrectly predicted match, especially the first and last indices of the list.