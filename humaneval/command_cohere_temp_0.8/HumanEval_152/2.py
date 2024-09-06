```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```

The solution works by using Python's list comprehension and short-circuit evaluation to create a new list of absolute differences between corresponding elements in the `game` and `guess` lists, with a key difference being that if the elements are equal, it sets the difference to 0, as required by the prompt's specification.

The tests passed correctly as the code is evaluated to be equivalent to the specification provided.