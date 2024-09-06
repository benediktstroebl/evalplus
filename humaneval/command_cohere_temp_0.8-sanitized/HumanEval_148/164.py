def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, pole in enumerate(planets):
        if pole == planet1:
            p1 = i
        if pole == planet2:
            p2 = i
    res = []
    if 0 <= p1 <= p2 < len(planets) :
        for pole in planets[p1+1:p2+1]:
            res.append(pole)
    return res if res else tuple()