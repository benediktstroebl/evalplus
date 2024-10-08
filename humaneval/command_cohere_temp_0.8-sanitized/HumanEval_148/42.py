def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, cur_planet in enumerate(planets):
        if cur_planet == planet1: p1 = i
        if cur_planet == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return tuple(planets[p1 + 1 : p2])