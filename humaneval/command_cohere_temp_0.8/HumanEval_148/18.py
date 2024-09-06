```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = None
    p2 = None
    for p in range(8):
        if planets[p] == planet1:
            p1 = p
        if planets[p] == planet2:
            p2 = p
    if p1 is None or p2 is None:
        return ()
    return (planets[p1:p2+1]).sort()
```

The function `bf` takes in two strings, `planet1` and `planet2`, and returns a tuple of strings of the planets between the two inputs. The function first creates an array of the planets and loops through the array to find the indices of the planets using the `planet1` and `planet2` inputs. If the `planet1` or `planet2` inputs are incorrect, the function returns an empty tuple. If the planets are correct, the function returns a tuple of the planets sorted by their proximity to the sun. 

Here is an example function call:
```python
 bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
```

And here is the expected outcome of the example.

Please note that the script assumes that the input is valid and the function does not perform any validation on the inputs, besides checking if the inputs are valid planet names.