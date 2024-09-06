```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
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
Which would be the correct solution for the test cases provided. 
Another example:
```python
game = [0, 5, 0, 0, 0, 4]
guess = [4, 1, 1, 0, 0, -2]
print(compare(game, guess))
```
This will output:
```
[4, 4, 1, 0, 0, 6]
```
Which is the correct solution for the second test case. The function could be optimized to use Python's `map` function instead of a list comprehension, but the underlying logic remains the same. 
Please note that the code assumes that the input arrays are valid and adhere to the specified constraints. It's the responsibility of the user to ensure the input aligns with the expected format and constraints when running the function in an actual environment. 
Let me know if you have any doubts or would like to discuss further! 
Enjoy the day!