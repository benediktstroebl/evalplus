def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planet1.lower() if planet1 in planets else None
    p2 = planet2.lower() if planet2 in planets else None
    
    if p1 and p2:
        res = []
        for i in range(8):
            if planets[i] == p1 and planets[i] != p2:
                res.append(planets[i])
                res.extend(bf(planets[i], planet2))
        return res or None
    else:
        return []