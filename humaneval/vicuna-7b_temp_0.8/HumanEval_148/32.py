
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
    # create a dictionary of planets and their distances from the sun
    planets = {"Mercury": 0.390, "Venus": 0.723, "Earth": 1.000, "Mars": 1.524, "Jupiter": 5.203, "Saturn": 9.567, "Uranus": 19.225, "Neptune": 30.059}
    # check if the planets are valid
    if not planet1 in planets or not planet2 in planets:
        return ()
    # check the orbits of the planets
    if planet1 > planet2:
        planet1, planet2 = planet2, planet1
    # sort the planets by their distance to the sun
    planets = sorted((planets[planet1], planet2), key=lambda x: x[0])
    # return the closest planets
    return (planets[0], planets[1]) if len(planets) < 3 else (planets[2], planets[3])
