
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
    e1, planet1, d1 = planet1, {}, 0
    e2, planet2, d2 = planet2, {}, 0
    planets = set(["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"])
    for planet in planets:
        if planet1 in planets and planet2 in planets:
            if planet1 == planet2: return planet1
            elif planet1 == e1: e1 = planet2
            elif planet1 == e2: e2 = planet2
            elif planet1 == planet2: return planet1
            planet1, planet2 = planet2, planet1
        elif planet1 in planets: planet1 = planet
        elif planet2 in planets: planet2 = planet
    if planet1 in planets and planet2 in planets:
        if planet1 == planet2: return planet1
        elif planet1 == e1: e1 = planet2
        elif planet1 == e2: e2 = planet2
        elif planet1 == planet2: return planet1
    if planet1 in planets: planet1 = e1
    elif planet2 in planets: planet2 = e2
    return e1, e2
