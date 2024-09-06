
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

    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 in planets and planet2 in planets:
        for planet in planets:
            if planet == planet1 or planet == planet2:
                continue
            else:
                if bf(planet1, planet) < bf(planet2, planet) and bf(planet1, planet) > bf(planet, planet2):
                    return tuple((planet, planet2))
                elif bf(planet1, planet) > bf(planet2, planet) and bf(planet1, planet) < bf(planet, planet2):
                    return tuple((planet, planet2))
                elif bf(planet1, planet) == bf(planet2, planet) and bf(planet1, planet) == bf(planet, planet2):
                    return tuple((planet, planet2))
    else:
        return ()
