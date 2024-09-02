
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

    # check if the input is valid
    if not is_valid_planet_name(planet1) or not is_valid_planet_name(planet2):
        return ()

    # check if the planets are between the other two planets
    if planet1 > planet2:
        b1, b2 = planet1, planet2
    else:
        b1, b2 = planet2, planet1

    # check if the planets are in the right order
    if b1 > b2:
        # sort the list of planets
        b1, b2 = b2, b1

    # get all the planets
    planets = sorted([b1, b2], key=lambda x: (x.get_distance_to_the_sun(), x.get_name()))

    return planets
