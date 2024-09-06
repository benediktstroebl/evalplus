```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
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
The code demonstrates basic Python principles, such as list comprehension, filtering, and explicit return. To see the underlying concepts and how the solution leverages them, feel free to browse the documentation on relevant topics:
1. **List Compression (`zip`):** This solution leverages list compression via the `zip` function to pair each element in `game` with the corresponding element in `guess`. 
2. **Filtering (`if x != y ...`):** The solution filters the list of pairs to only store the difference if the elements are not equal. This is done using Python's filtering conditionals.
3. **Absolute Value (`abs`):** To ensure a positive result, the difference is wrapped in the `abs` function, which returns the distance from zero for any given number. 

These are foundational Python concepts and this solution demonstrates their application in a practical problem context. Feel free to consult these concepts in the Python documentation for more in-depth understanding. Let me know if you'd like further clarification! 
<|END MARKDOWN|>