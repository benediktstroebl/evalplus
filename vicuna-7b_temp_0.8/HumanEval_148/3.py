
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

    if not correct_planet_name(planet1) or not correct_planet_name(planet2):
        return ()

    # get the orbits of the two planets
    orbit1 = get_orbit(planet1)
    orbit2 = get_orbit(planet2)

    # get the orbit of the other planet
    orbit_other = get_orbit(planet2) if orbit1 < orbit2 else get_orbit(planet1)

    # calculate the distance between the two orbits
    distance = abs(orbit1.semi_major_axis - orbit2.semi_major_axis)

    # get the closest planet to the other planet
    closest_planet = get_closest_planet(orbit_other)

    # get the list of all planets
    all_planets = get_all_planets()

    # return a tuple of all planets whose orbits are located between the orbit of planet1 and the orbit of planet2
    return all_planets[orbit1.semi_major_axis < orbit2.semi_major_axis and orbit1.semi_major_axis < orbit_other.semi_major_axis]
