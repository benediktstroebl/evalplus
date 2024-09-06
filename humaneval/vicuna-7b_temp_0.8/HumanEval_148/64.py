
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
    # check if the planets are valid
    if not is_valid_planet(planet1) or not is_valid_planet(planet2):
        return ()
    
    # list of planets
    planets = [planet1, planet2]
    # sort the planets by their distance from the sun
    planets.sort(key=lambda x: x.distance_to(sun))
    
    # list of planets between the two given planets
    result = []
    for i in range(len(planets) - 1):
        # check if the planet's orbit is between the two given planets
        if planets[i].distance_to(sun) < planets[i + 1].distance_to(sun):
            result.append(planets[i])
        elif planets[i].distance_to(sun) > planets[i + 1].distance_to(sun):
            result.append(planets[i + 1])
    
    # sort the result by proximity to the sun
    result.sort(key=lambda x: x.distance_to(sun))
    
    return result
