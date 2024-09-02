
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
    # check if the planets are correct
    if not is_correct_planet_name(planet1) or not is_correct_planet_name(planet2):
        return ()

    # get the orbit of planet1 and planet2
    planet1_orbit = get_orbit(planet1)
    planet2_orbit = get_orbit(planet2)

    # sort the planets by their proximity to the sun
    planet_list = get_planets()
    planet_list.sort(key=lambda x: (x.semi_major_axis, x.distance, x.barycenter))

    # get the indices of the planets
    planet1_index = np.where(planet1_orbit == planet_list)[0][0]
    planet2_index = np.where(planet2_orbit == planet_list)[0][0]

    # get the indices of the planets between the orbit of planet1 and planet2
    planet1_index = np.where(planet1_orbit < planet2_orbit)[0][0]
    planet2_index = np.where(planet2_orbit < planet1_orbit)[0][0]

    return planet_list[planet1_index:planet2_index+1]
