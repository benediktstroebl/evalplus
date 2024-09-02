
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
    planet_dict = {
        "Mercury": 0,
        "Venus": 1,
        "Earth": 2,
        "Mars": 3,
        "Jupiter": 4,
        "Saturn": 5,
        "Uranus": 6,
        "Neptune": 7,
    }

    if planet1 in planet_dict and planet2 in planet_dict:
        planets = planet_dict.keys()
        if planet_dict[planet1] < planet_dict[planet2]:
            planets = planets[planet_dict[planet1] : planet_dict[planet2] + 1]
        elif planet_dict[planet2] < planet_dict[planet1]:
            planets = planets[planet_dict[planet2] : planet_dict[planet1] + 1]
        else:
            return ()
        return tuple(planets)
    return ()
