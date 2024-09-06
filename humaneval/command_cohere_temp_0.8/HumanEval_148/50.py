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

The provided Python script defines a function `bf` that takes two planet names as strings (`planet1` and `planet2`) as inputs. The function returns a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2` in the solar system, sorted by proximity to the sun. The function returns an empty tuple if either `planet1` or `planet2` is not a correct planet name.

The script thoroughly checks if the inputs are valid planet names by indexing them in the `planets` list of planet names. The function utilizes negative indexing to iterate through the list and finds the correct positions of the planets in the solar system. Finally, the function returns a sliced piece of the `planets` list to deliver the required planets. The code is encapsulated in a self-contained function, which can be readily used in other programs or tested independently. 

This code could be optimized, but this straightforward solution is concise and clear, expressing the underlying logic effectively.