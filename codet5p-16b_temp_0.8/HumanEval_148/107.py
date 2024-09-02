
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

    planets = {
        "Mercury" : 0.387,
        "Venus" : 0.723,
        "Earth" : 1,
        "Mars" : 1.524,
        "Jupiter" : 5.204,
        "Saturn" : 9.532,
        "Uranus" : 19.213,
        "Neptune" : 30.061
    }

    if planet1 in planets and planet2 in planets:
        distance1 = planets[planet1]
        distance2 = planets[planet2]
        difference = abs(distance1 - distance2)
        result = []
        for key, value in planets.items():
            if distance1 < distance2 and (distance1 <= value <= distance2):
                result.append(key)
        return tuple(result)
    return ()



