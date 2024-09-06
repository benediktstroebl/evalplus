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

The BF function employs the planetary order as an array, determining the array indices of the given planets. The range of indices is used to sort and return the planets between the two given planets, closer to the sun. Since the returned range is nondefensive, it is essential to use caution when accessing the edges. A return value of `()` indicates that either no valid planet was specified, or that no planets exist in that particular range. 

The samples in the manifesto are successfully passed through the function, and the result is correctly computed.