def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = None
    p2 = None
    fl = False
    for i in range(8):
        if planets[i] == planet1:
            p1 = planets[i]
            fl = True
        if planets[i] == planet2:
            p2 = planets[i]
            fl = True
        if p1 and p2:
            break
    if fl == False:
        return ()
    res = []
    cnt = 0
    for i in range(8):
        if planets[i] != p1 and planets[i] != p2:
            if planets[i] >= p1 and planets[i] <= p2:
                res.append(planets[i])
                cnt += 1
        if p1 >= p2:
            break
    return tuple(res[::-1]) if cnt > 0 else ()