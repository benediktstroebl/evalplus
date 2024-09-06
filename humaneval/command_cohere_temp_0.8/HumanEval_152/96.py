```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```

This Python script provides a function that takes two arguments, `game` and `guess`, and returns an array of the same length denoting how far off each guess was. If they have guessed correctly, the value is 0, and if not, the value is the absolute difference between the guess and the score. The provided example and test cases demonstrate how to use the function and show its correct behavior. 
To use this function, you can call it by providing two arrays as arguments `game` and `guess`, as shown in the examples below:
```python
print(compare([1,2,3,4,5,1], [1,2,3,4,2,-2]))
print(compare([0,5,0,0,0,4], [4,1,1,0,0,-2]))
``` 
This should print:
```
[0, 0, 0, 0, 3, 3]
[4, 4, 1, 0, 0, 6]
``` 

Let's break down the code:
```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```

Here's a breakdown of the code within the function:
1. `result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]` - This line uses a list comprehension with conditional checking. It iterates over pairs of corresponding elements `(x, y)` from the `game` and `guess` arrays. It calculates the absolute difference `abs(x-y)` between these elements and stores this difference in the `result` list if the elements are not equal `(x != y)`. If the elements are equal, it assigns 0 to the corresponding index of the `result` list. 
2. `return result` - The function returns the `result` list, which contains the computed differences or zeros denoting correct guesses. 

In summary, this code solves the problem by iterating through the game and guesses and calculating the absolute difference between the two for each index of the two arrays. It returns these differences, or zeros if the guess was correct. 

You can use this code by calling the `compare` function with two lists as arguments to get the result back from the function. Frontend Development and Python are both well-known technologies for building web applications. Python is an adaptable language that is used in a variety of contexts and is well-known for its simplicity and readability. When working with frontend applications, Python is frequently used for tasks such as data analysis, machine learning, and server-side development.

It's important to note that the above code snippet assumes that the two input arrays `game` and `guess` are of equal length and correctly aligns them for iteration. If the input arrays are not of equal length or properly aligned, the comparison may not work as expected.