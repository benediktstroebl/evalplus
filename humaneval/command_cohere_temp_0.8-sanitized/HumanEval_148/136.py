def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = None
    p2 = None
    idx1 = planets.index(planet1) if planet1 in planets else -1
    idx2 = planets.index(planet2) if planet2 in planets else -1
    if idx1 >= 0 and idx2 >= 0:
        p1 = planets[idx1]
        p2 = planets[idx2]
        result = []
        l = max(idx1, idx2)
        r = min(idx1, idx2)
        if l == idx1 and r == idx2:
            return ()
        for i in range(l, r + 1):
            if planets[i] not in result:
                result.append(planets[i])
        return tuple(result)
    else:
        return ()