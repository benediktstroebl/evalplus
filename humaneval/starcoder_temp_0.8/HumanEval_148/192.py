
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
    orbits = {"Mercury": (108, 149), "Venus": (149, 224), "Earth": (227, 365), "Mars": (354, 687), "Jupiter": (718, 42986), "Saturn": (1427, 120110), "Uranus": (2871, 579000), "Neptune": (4531, 681900)}
    if planet1 not in orbits or planet2 not in orbits:
        return ()
    else:
        i1 = orbits[planet1][0]
        j1 = orbits[planet1][1]
        i2 = orbits[planet2][0]
        j2 = orbits[planet2][1]
        return sorted(orbits.keys(), key = lambda x: min(abs(orbits[x][0] - i1), abs(orbits[x][1] - j1)) + min(abs(orbits[x][0] - i2), abs(orbits[x][1] - j2)))
