
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
    planets = {"Mercury": 0.387, "Venus": 0.723, "Earth": 1.0, "Mars": 1.524, "Jupiter": 5.204, "Saturn": 9.583, "Uranus": 19.218, "Neptune": 30.105}
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        i = 0
        while planets[planet2] < planets[planet1]:
            i += 1
            planet2 = sorted(planets.keys())[i]
        return tuple([planet for planet in sorted(planets.keys())[i:] if planets[planet] > planets[planet1] and planets[planet] < planets[planet2]])
