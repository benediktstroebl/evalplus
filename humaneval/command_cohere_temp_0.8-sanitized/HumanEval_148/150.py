def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = None
    p2 = None
    idx1 = None
    idx2 = None
   
    for i, p in enumerate(planets):
        if p == planet1:
            p1 = i
        if p == planet2:
            p2 = i
            planet2_idx = p2
            break
    
    if p1 is None or p2 is None:
        return ()
      
    for i, p in enumerate(planets):
        if i < p1:
            continue
        if i > p2:
            break
        idx1 = i
    
    return (planets[idx1:p2_idx])