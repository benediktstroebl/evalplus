```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length lists, `game` and `guess`, where each element corresponds to the real result of a match and the guessed result. It returns a list where each element is the absolute difference between the two lists, if the guess is incorrect, or 0 if the guess is correct. 

The behavior of the function can be explained by the following loop:
```python
return [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
```
For each pair of corresponding elements `x` from `game` and `y` from `guess`, the function checks if `x` is not equal to `y`. In that case, it calculates the absolute difference between `x` and `y`, and returns it as the corresponding element in the output list. If `x` is equal to `y`, it returns 0, indicating that the guess was correct for this match. The `zip` function is used to iterate through pairs of corresponding elements from both lists.

Here is an example use case of the previously mentioned function:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
print(compare(game, guess))
```
This would print:
```
[0, 0, 0, 0, 3, 3]
```

Here's the full Python script with additional functions to showcase the use of the `compare` function:
```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]

def main():
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 2, -2]
    print("Real results: ", game)
    print("Guessed results: ", guess)
    print("Difference between the two:")
    print(compare(game, guess))

def main_test():
    # Test case 1
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 2, -2]
    correct_output = [0, 0, 0, 0, 3, 3]
    print(correct_output == compare(game, guess))

    # Test case 2
    game = [0, 5, 0, 0, 0, 4]
    guess = [4, 1, 1, 0, 0, -2]
    correct_output = [4, 4, 1, 0, 0, 6]
    print(correct_output == compare(game, guess))

main_test()
main()
```

The tests prove the correctness of the `compare` function in the given scenario.