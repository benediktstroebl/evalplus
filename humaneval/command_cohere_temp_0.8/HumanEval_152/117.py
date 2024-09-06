```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```

The function employs a list comprehension, which is a powerful feature in Python used to create a new list from a variety of sources. Here, it is used to create a new list by comparing each element of the `game` and `guess` lists individually. The `abs(x-y)` function calculates the absolute difference between the two values, effectively determining how far off the guess was. The `if` statement checks if the elements are equal, in which case it sets the value to 0, denoting a correct guess.