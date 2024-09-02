
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
    planet_orbits = {
        "Mercury": 57.91,
        "Venus": 108.21,
        "Earth": 149.6,
        "Mars": 227.94,
        "Jupiter": 778.34,
        "Saturn": 1427,
        "Uranus": 2872,
        "Neptune": 4498,
    }
    if planet1 not in planet_orbits or planet2 not in planet_orbits:
        return ()
    elif planet1 == planet2:
        return ()
    else:
        return tuple(sorted(planet_orbits, key=lambda x: abs(x - planet_orbits[planet1])))[planet_orbits[planet1]:planet_orbits[planet2] + 1]

