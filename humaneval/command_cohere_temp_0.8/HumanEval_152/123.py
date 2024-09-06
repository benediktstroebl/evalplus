```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It returns an array of the same length as the input arrays, where each element represents the difference between the corresponding elements in the `game` and `guess` arrays. If the guess was correct, the value is 0, otherwise, it is the absolute difference between the guess and the score. This accurately solves the problem statement, and the function is self-contained and standalone. 
The returned list is constructed using a list comprehension that iterates through the corresponding elements of `game` and `guess`. For each pair of elements, it calculates the absolute difference (`abs()`) between them. If they match (i.e., the guess was correct), it assigns 0 to that element in the resulting list. 
The script returns the resulting list, which accurately solves the problem statement. 
Here is an example of how to use this function:
```python
print(compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2,-2]))
```
This will output:
```
[0, 0, 0, 0, 3, 3]
```
Which demonstrates the function's ability to determine how far off each guess was in the example scenario.