```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the score of a match, and returns an array of the same length containing the absolute difference between the guess and the score if the guess is incorrect, and 0 if the guess is correct. 

Here is an example usage of the function:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
print(compare(game, guess))
```
This will output:
```
[0, 0, 0, 0, 3, 3]
```
The example shown in the problem statement demonstrates how the function behaves for the given inputs and reveals the desired output. 
If you want to test the function with more examples, feel free to add more test cases with different inputs. Hoping this solution aids you further in your tasks, I remain at your disposal for any clarifications or further information you may require. Feel free to ask follow-up questions.