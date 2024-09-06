def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)

    res = []
    for i in range(p1 + 1, p2 + 1):
        res.append(planets[i])

    return res if res != [] else None