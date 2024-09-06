```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```

The solution works by using Python's built-in `zip()` function to iterate over each element of `game` and `guess` simultaneously. In doing so, each pair of corresponding elements is retrieved and can be easily compared. We then use a list comprehension to check if each pair has the same value (`x != y`), and if so, we calculate the absolute difference (`abs(x-y)`) and store it in the `result` list. If they have the same value, we simply put `0` in the list. The result is then returned at the end. 

This approach makes use of the powerful `zip()` function in Python, which makes it easy to iterate through multiple arrays simultaneously. List comprehensions are then used to transform and filter the data, providing an elegant solution to the problem.