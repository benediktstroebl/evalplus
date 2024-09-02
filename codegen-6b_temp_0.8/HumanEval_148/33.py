
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
    PA = Planets.planet_abbreviation
    PLANETS = Planets.all_planets

    if planet1 not in PLANETS or planet2 not in PLANETS:
        return ()
    else:
        planet_index = PLANETS.index(planet1)
        planet_index2 = PLANETS.index(planet2)
        all_planets = (Planets[i] for i in xrange(planet_index, planet_index2+1))
        return tuple(all_planets)
