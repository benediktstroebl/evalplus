def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planet1.lower() if planet1 in planets else ''
    p2 = planet2.lower() if planet2 in planets else ''
    res = []
    s1, s2 = 0, 7
    while s1 <= s2:
        mid = (s1 + s2) // 2
        if planets[mid] == p1:
            s2 = mid - 1
        elif planets[mid] == p2:
            s1 = mid + 1
        else:
            res.append(planets[mid])
    return res if res else tuple()