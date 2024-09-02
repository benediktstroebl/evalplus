
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
    planets = [('Mercury', 57900000), ('Venus', 108200000), ('Earth', 149600000), 
    ('Mars', 227900000), ('Jupiter', 778600000), ('Saturn', 1429400000), 
    ('Uranus', 2870900000), ('Neptune', 4495100000)]
    if planet1 not in [x[0] for x in planets] or planet2 not in [x[0] for x in planets]:
        return ()
    planet1_idx = [x[0] for x in planets].index(planet1)
    planet2_idx = [x[0] for x in planets].index(planet2)
    if planet1_idx < planet2_idx:
        result = [x[0] for x in planets[planet1_idx+1:planet2_idx]]
    else:
        result = [x[0] for x in planets[planet1_idx:planet2_idx+1]]
    return tuple(result)


