
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
    res = []
    # get distances
    planet1_dist = get_dist(planet1)
    planet2_dist = get_dist(planet2)
    if planet1_dist == None or planet2_dist == None:
        return res
    # now get all planets in the system
    planets = get_planets()
    # cycle through all planets
    for planet in planets:
        if get_dist(planet) in range(planet1_dist, planet2_dist + 1):
            res.append(planet)
    return tuple(sorted(res))
    
    