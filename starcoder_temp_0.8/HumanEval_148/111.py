
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
    # let's handle some trivial cases
    if planet1 == planet2:
        return tuple()
    elif planet1 not in planets or planet2 not in planets:
        return tuple()
    else:
        # use the get_orbit method to get the orbits in which the two planets 
        # are located
        orbit1 = get_orbit(planet1)
        orbit2 = get_orbit(planet2)
        # find the common orbit between the two orbits
        common_orbit = orbit1[0:orbit1.index(orbit2[0])]
        # create a list of planets sorted by their proximity to the sun
        planet_list = [p for p in planets if get_orbit(p)[0] in common_orbit]
        planet_list.sort(key=lambda x: planets.index(x))
        return tuple(planet_list)
    
