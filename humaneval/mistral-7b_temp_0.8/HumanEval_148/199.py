
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
    def in_range(planet, planet1, planet2):
        if planet == planet1:
            return True
        if planet == planet2:
            return True
        elif planet1 < planet < planet2:
            return True
        return False
    # is in range?
    if in_range(planet1, "Mercury", "Neptune"):
        # is in range?
        if in_range(planet2, "Mercury", "Neptune"):
            return tuple(planets)
        else:
            return tuple()
    else:
        return tuple()
