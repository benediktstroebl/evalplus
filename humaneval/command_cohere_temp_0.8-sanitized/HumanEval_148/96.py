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
            fl = True    
    if not fl:
        return ()
    if p2 < p1:
        temp = p2
        p2 = p1
        p1 = temp
    res = []
    if p1 > 0:
        res.append(planets[p1 - 1])
    if p2 < 7:
        res.append(planets[p2 + 1])
    return tuple(res)