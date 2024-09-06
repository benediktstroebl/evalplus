```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the score of a match, and returns an array of the same length containing the absolute difference between the guess and the score for each element, or 0 if the guess was correct. 

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
The example corresponds to the example provided in the prompt. The return value is an array denoting how far off each guess was. If they had guessed correctly, the value is 0, and if not, the absolute difference between the guess and the score. 

This function solves the problem using a list comprehension, which is a powerful Python construct for creating lists by applying transformations to each item in a sequence. Here's how it works:
- `abs(x-y) if x != y else 0` This part takes the absolute difference between each element in the `game` array and the corresponding element in the `guess` array. If the elements are not equal, which means the guess was incorrect, it returns the absolute difference. If the elements are equal, which means the guess was correct, it returns 0.
- `return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]` This part uses the `zip` function to create a tuple with corresponding elements from the `game` and `guess` arrays. It then applies the transformation defined in the first part to each element in the tuple and collects the results in a list, which is then returned as the final result. 
Make sure to install the necessary dependency for the `zip` function, which is included in Python 3 by default. If you are running Python 2, you may need to add `from future import zip` at the start of your code. In the example, we demonstrate the usage of the function with the provided example from the prompt and print the returned array.  The result shows how far off each guess was from the corresponding score in the `game` array.  If the guess was correct, it outputs `0`, and if not, it outputs the absolute difference between the guess and the score.