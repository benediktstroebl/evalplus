def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = None
    p2 = None
    fl = False
    for i in range(8):
        if planets[i] == planet1:
            p1 = planets[i]
            fl = True
            break
        if planets[i] == planet2:
            p2 = planets[i]
            fl = True
            break
    if not fl:
        return ()
    if p2 == p1:
        return (p2)
    planets_bf = []
    if p1 > p2:
        for i in range(p2, p1):
            planets_bf.append(planets[i])
    else:
        for i in range(p1, p2):
            planets_bf.append(planets[i])
    return tuple(planets_bf)