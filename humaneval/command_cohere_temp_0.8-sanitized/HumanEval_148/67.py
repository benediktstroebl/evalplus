def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = None
    p2 = None
    ans = []
    for p in range(8):
        if planets[p] == planet1:
            p1 = p
        if planets[p] == planet2:
            p2 = p
        if p1 is not None and p2 is not None:
            if p1 < p2:
                ans += planets[p1:p2 + 1]
            else:
                ans += planets[p2:p1 + 1]
            break
    return ans if len(ans) > 0 else tuple()