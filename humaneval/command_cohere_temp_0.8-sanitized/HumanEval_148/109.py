def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = None
    p2 = None
    for i, val in enumerate(planets):
        if val == planet1:
            p1 = i
        if val == planet2:
            p2 = i
    if p1 is None or p2 is None:
        return tuple()
    a = p1 > p2
    res = []
    cnt = p2 - p1
    while cnt > 0:
        if a:
            res.append(planets[p1])
            p1 -= 1
        else:
            res.append(planets[p2])
            p2 -= 1
        cnt -= 1
    return tuple(res[::-1])