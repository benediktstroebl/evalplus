def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planet1.lower() if planet1 in planets else ''
    p2 = planet2.lower() if planet2 in planets else ''
    result = []
    if p1 and p2:
        for planet in planets:
            if planet == p2 and planet != p1:
                break
            if planet == p1:
                continue
            result.append(planet)
        result.sort(key=lambda x: planets.index(x))
    return tuple(result)