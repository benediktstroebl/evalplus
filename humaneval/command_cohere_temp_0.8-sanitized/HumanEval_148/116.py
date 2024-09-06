def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = None
    p2 = None
    fl = False
    for i in range(8):
        if planets[i] == planet1:
            p1 = planets[i]
            fl = True
        if planets[i] == planet2:
            p2 = planets[i]
            fl = True
        if p1 and p2:
            break
    if not fl:
        return ()
    if p1 == p2:
        return (p1)
    result = []
    p1index = planets.index(p1)
    p2index = planets.index(p2)
    for i in range(p1index + 1, p2index + 2):
        result.append(planets[i])
    return tuple(result)