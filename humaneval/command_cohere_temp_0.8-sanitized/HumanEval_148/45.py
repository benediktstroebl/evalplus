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
        return ()
    l = []
    while p1 <= p2:
        if p1 <= 7 and p2 >= 7:
            break
        if p1 == p2:
            l.append(planets[p1])
        elif p1 < p2:
            l.append(planets[p1])
            p1 += 1
        else:
            p2 -= 1
        if p1 <= 6 and p2 >= 6:
            l.append(planets[p1])
            p1 += 1
        elif p1 <= 5 and p2 >= 7:
            l.append(planets[p2])
            p2 -= 1
    return tuple(l)