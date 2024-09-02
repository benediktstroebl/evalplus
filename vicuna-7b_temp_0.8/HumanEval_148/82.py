
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
    # determine the orbits of the planets
    orbit1 = get_orbit(planet1)
    orbit2 = get_orbit(planet2)

    # calculate the proximity of each planet
    proximity1 = proximity(orbit1, orbit2)
    proximity2 = proximity(orbit2, orbit1)

    # sort the planets by proximity to the sun
    sorted_planets = sorted(enumerate(orbit1), key=lambda x: x[1])
    sorted_planets.reverse()

    # return the sorted list of planets
    return tuple(sorted_planets)
