def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planet1.lower() if planet1 in planets else ''
    p2 = planet2.lower() if planet2 in planets else ''
    result = []
    if p1 and p2:
        for i in range(8):
            if planets[i] == p2 and planets[i] != p1:
                result.append(planets[i])
                break
            elif planets[i] == p1 and planets[i] > p2:
                result.append(planets[i])
                for j in range(i + 1, 8):
                    if planets[j] == p2 and planets[j] != planets[i]:
                        result.append(planets[j])
                        break
            elif planets[i] < p2:
                break
    return result if result else tuple()