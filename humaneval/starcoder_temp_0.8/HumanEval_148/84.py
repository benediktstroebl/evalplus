
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    
    planets = {
        "Mercury": 0.38,
        "Venus": 0.72,
        "Earth": 1.00,
        "Mars": 1.52,
        "Jupiter": 5.20,
        "Saturn": 9.54,
        "Uranus": 19.20,
        "Neptune": 30.05
    }
    if planet1 not in planets or planet2 not in planets:
        return ()
    p1 = planets[planet1]
    p2 = planets[planet2]
    out = []
    for planet, period in planets.items():
        if period >= p1 and period <= p2:
            out.append(planet)
    return tuple(sorted(out))
