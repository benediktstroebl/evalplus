```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```

The function uses a list comprehension, which is a powerful construct in Python that allows you to create a new list by applying a conditional test or operation to each item in a sequence. In this case, it creates a new list `result` where each element is the absolute difference between the corresponding elements of `game` and `guess`, if they are different, otherwise, it is set to 0 which represents a correct guess. 

The `zip` function is used to iterate over the corresponding elements of both arrays `game` and `guess`. 

This solution passes the test cases provided for this problem with correct edge cases and behavior.