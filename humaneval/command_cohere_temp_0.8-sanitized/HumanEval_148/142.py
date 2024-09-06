def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, cur_planet in enumerate(planets):
        if cur_planet == planet1:
            p1 = i
        if cur_planet == planet2:
            p2 = i
    res = []
    if 0 <= p1 < p2:
        for i in range(p1 + 1, p2 + 1):
            res.append(planets[i])
    elif p2 < p1 <= 7:
        for i in range(p2 + 1, p1 + 1):
            res.append(planets[i])
    return res if res else ()