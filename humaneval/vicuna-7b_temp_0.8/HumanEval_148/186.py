
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
    # use a list of the eight planets
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    # check if the planets are valid
    if planet1 not in planets or planet2 not in planets:
        return ()

    # check the orbits of the planets
    orbit1 = get_orbit(planet1)
    orbit2 = get_orbit(planet2)

    # get the difference between the orbits
    distance = orbit2 - orbit1

    # sort the planets by their distance from the sun
    sorted_planets = sorted(planets, key=lambda x: abs(x - orbit1))

    # return the list of planets
    return sorted_planets[int(len(sorted_planets) * (orbit2.semi_major_axis - orbit1.semi_major_axis) / distance)]
