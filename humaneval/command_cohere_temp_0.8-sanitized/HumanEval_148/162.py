def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = None
    p2 = None
    idx1 = None
    idx2 = None
   
    for i, val in enumerate(planets):
        if val == planet1:
            p1 = i
        if val == planet2:
            p2 = i
            
    if p1 is not None and p2 is not None:
        idx1 = planets.index(planet1)
        idx2 = planets.index(planet2)
        
        res = []
        l = max(idx1, idx2)
        r = min(idx1, idx2)
        
        for i in range(l, r + 1):
            if i == idx1 or i == idx2:
                continue
            res.append(planets[i])
            
        return res if res else None
    else:
        return None