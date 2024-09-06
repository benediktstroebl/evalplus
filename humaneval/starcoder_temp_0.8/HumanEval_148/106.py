
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
    p = {"Mercury": 57910000, "Venus": 108200000, "Earth": 149600000, "Mars": 227940000, "Jupiter": 778400000, "Saturn": 1433400000, "Uranus": 2870990000, "Neptune": 4504000000}
    if planet1 in p and planet2 in p:
        return tuple(sorted([k for k, v in p.items() if v > p[planet1] and v < p[planet2]]))
    else:
        return ()
    
