```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```

The Python script provides a function `compare` which takes in two arrays `game` and `guess` and returns an array of the same length denoting how far off each guess was. If they have guessed correctly, the value is 0, and if not, the value is the absolute difference between the guess and the score. The function is designed to be self-contained and does not rely on any external variables or assumptions. 

The function works by using a list comprehension, which goes through each element in the `game` and `guess` array and compares them. Using the `zip` function, it pairs each element in `game` and `guess` together and checks if the guess was correct by taking the absolute difference (`abs`) between the two elements. If the guess was correct, it sets the value to 0. It repeats this process for each pair of elements and compiles the result in a list, which it then returns as `result`. 

The code above is a self-contained Python script that solves the problem using a straightforward approach, and it passes the given tests. It utilizes core Python principles such as list comprehension and the `zip` function to solve the problem efficiently.

The code could be improved by explaining the purpose of the function, mentioning that it returns an array of how far off each guess was, and mentioning that it uses absolute difference if the guess was incorrect, which could be referenced in the code with an emphatic comment like `# Emitting the difference if the guess is incorrect`. It also does not handle the case when the lengths of `game` and `guess` are not equal, which might be a logical edge case to handle. It could also have an initial comment summarizing the problem for context, and the `example` comment could be included as well. Here is a revised version of the code: 

```python
# Summarizes the moment when one sees the results of a match and realizes how far off the guess was
def compare(game, guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.

    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.

    example:
    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
```