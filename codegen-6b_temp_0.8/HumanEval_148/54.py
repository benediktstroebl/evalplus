
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
    if planet1 not in PLANETS:
        return tuple()
    if planet2 not in PLANETS:
        return tuple()

    planet1_pos = PLANETS.index(planet1)
    planet2_pos = PLANETS.index(planet2)
    common_ancestor = set(PLANETS).intersection(set(bf_helper(planet1_pos, PLANETS), bf_helper(planet2_pos, PLANETS)))
    return tuple(sorted(common_ancestor))

