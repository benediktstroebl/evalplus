```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, cur_planet in enumerate(planets):
        if cur_planet == planet1: p1 = i
        if cur_planet == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return (planets[p1:p2+1])
```

The provided Python script defines a function called `bf` that takes two parameters, `planet1` and `planet2`. This function returns a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by proximity to the sun. The function first creates a list of all eight planets and then finds the indices of `planet1` and `planet2` in this list. If either of these planets is not found in the list, the function returns an empty tuple. Otherwise, it returns a tuple of planets formed by the planets in the range from `planet1` to `planet2`, inclusive, sorted by their positions in the list, which corresponds to their proximity to the sun. This solution is specified in a corresponding markdown code block. 

The examples provided in the problem statement show how the function works for different input scenarios. Let's break down the solution step by step and explain each part:
1. **Variable Initialization**:
   - `planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']`: This line creates a list called `planets` containing the names of the eight planets in our solar system, ordered by their proximity to the sun.
2. **Finding Indices of Input Planets**:
   - `p1, p2 = -1, -1`: These are variable initializations for `p1` and `p2` which will store the indices of `planet1` and `planet2` in the `planets` list, respectively.
   - `for i, cur_planet in enumerate(planets)`: This starts a loop that iterates over the planets in the `planets` list. The `enumerate` function allows us to iterate over the list indexing each planet with the variable `i`.
   - `if cur_planet == planet1: p1 = i`: If the current planet in the loop matches the `planet1` input, the `p1` index is assigned the current index `i`.
   - `if cur_planet == planet2: p2 = i`: Similarly, if the current planet matches the `planet2` input, the `p2` index is assigned the current index `i`.
3. **Returning Result**:
   - `if p1 == -1 or p2 == -1: return ()`: If none of the planets are found in the list (if `p1` or `p2` remains -1), the function returns an empty tuple `()`. This handles the case where the input planets are not recognized or not in the list.
   - `return (planets[p1:p2+1])`: If the planets are found and their indices are determined, the function returns a tuple of planets formed by the elements of the `planets` list in the range from `p1` to `p2` (inclusive). The planets are sorted by their indices in the list, which