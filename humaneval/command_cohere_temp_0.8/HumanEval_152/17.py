```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length lists, game and guess, as arguments. It returns a list of the same length where each element is the absolute difference between the two lists if the guess is wrong, or 0 if the guess is correct. The absolute difference is calculated using the built-in `abs()` function, and the result is List comprehension is used to produce the return list based on these calculations. 

The `zip()` function is used to iterate over the elements of both lists in parallel, matching each element of game with the corresponding element of guess. This allows us to compare each pair of elements and compute the difference or determine correctness. 

This solution has a time complexity of O(n), where n is the length of the two lists, since it iterates through each element of both lists only once.

This approach uses only basic Python techniques, making it relatively efficient and straightforward. It also adheres to the problem's explanation, providing a clear and understandable solution.