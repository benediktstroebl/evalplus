def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    result = []
    for i in range(p1, p2 + 1):
        result.append(planets[i])
            
    return result if result != planets and planet1 in planets and planet2 in planets else tuple()