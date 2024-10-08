def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return ()
    i = planets.index(planet1)
    j = planets.index(planet2)
    if i > j:
        i, j = j, i
    return tuple(p for p in planets if i < planets.index(p) < j)
