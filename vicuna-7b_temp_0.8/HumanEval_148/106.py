
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
    # check if planets are valid
    if planet1 == "Mercury" or planet1 == "Venus" or planet1 == "Earth" or \
       planet1 == "Mars" or planet1 == "Jupiter" or planet1 == "Saturn" or \
       planet1 == "Uranus" or planet1 == "Neptune":
        return ()
    if planet2 == "Mercury" or planet2 == "Venus" or planet2 == "Earth" or \
       planet2 == "Mars" or planet2 == "Jupiter" or planet2 == "Saturn" or \
       planet2 == "Uranus" or planet2 == "Neptune":
        return ()
    
    # calculate distance between planets
    r1 = _get_distance(planet1)
    r2 = _get_distance(planet2)
    d = r2 - r1
    
    # calculate the closest planet
    closest_planet = _find_closest_planet(r1, r2, d)
    
    # calculate all planets whose orbit is between the orbit of planet1 and the orbit of planet2
    planets = _find_planets(r1, r2, closest_planet)
    
    # sort the planets by proximity to the sun
    planets = sorted(planets, key=lambda x: (x.distance_to(sun), x.name))
    
    return planets
