def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = None
    p2 = None
    fl = False
    for i in range(8):
        if planets[i] == planet1:
            p1 = i + 1
        if planets[i] == planet2:
            p2 = i + 1
        if p1 and p2:
            fl = True
            break
    if not fl:
        return ()
    res = []
    if p1 > p2:
        p1, p2 = p2, p1
    for i in range(p2, p1):
        res.append(planets[i])
    return tuple(res)