def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = None
    p2 = None
    for p in range(8):
        if planets[p] == planet1:
            p1 = p
        if planets[p] == planet2:
            p2 = p
    if p1 is None or p2 is None:
        return ()
    return tuple(planets[p] for p in range(max(p1, p2) + 1, min(p1, p2), -1))