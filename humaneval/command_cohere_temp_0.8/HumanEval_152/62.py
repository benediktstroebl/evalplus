```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It returns an array of the same length as these inputs, where each element represents the difference between the corresponding elements in the `game` and `guess` arrays. If the guess was correct, the result is 0, otherwise, it is the absolute difference between the guess and the score. 

Such a solution is concise and easy to understand, neatly fitting the requirements of the problem. It also nicely illustrates the expressive power of Python and its list comprehension capabilities.

This function can be tested as follows:
```python
# Test Case 1
print(compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]))
# Output: [0, 0, 0, 0, 3, 3]

# Test Case 2
print(compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]))
# Output: [4, 4, 1, 0, 0, 6]
```

The function should return the expected output for each test case based on the provided examples in the problem statement.