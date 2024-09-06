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
    return (planets[p1:p2+1]).sort()