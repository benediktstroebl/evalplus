
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
    # Check the input
    if not is_valid_planet_name(planet1) or not is_valid_planet_name(planet2):
        return ()

    # Get the position of the planets
    planet_pos = [(astronomical.Sun().arcsec(planet), planet) for planet in (planet1, planet2)]

    # Get all planets between the two given planets
    planets = sorted(planet_pos, key=lambda x: x[1], reverse=True)

    return tuple(planets[:-1])
