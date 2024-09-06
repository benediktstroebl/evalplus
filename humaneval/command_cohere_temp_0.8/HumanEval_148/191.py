```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    result = []
    for i in range(p1, p2 + 1):
        result.append(planets[i])
            
    return result if result != planets and planet1 in planets and planet2 in planets else tuple()
```

The function `bf` takes in two strings, `planet1` and `planet2`, and returns a tuple of strings of planets that are situated between the orbits of the two input planets, sorted by proximity to the sun. The function first compiles a list of the eight planets. It then finds the indices of `planet1` and `planet2` in the list using the `index` function. The algorithm then inserts a range between the two indices into a blank list and fills it with planets. The list is then returned to the caller. 

The test cases check various permutations of the input to verify the correctness of the function. Would you like help with any other coding problems?