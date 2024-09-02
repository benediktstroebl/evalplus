
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
    'Mercury': 0.387,
    'Venus': 0.723,
    'Earth': 1.000,
    'Mars': 1.524,
    'Jupiter': 11.862,
    'Saturn': 29.447,
    'Uranus': 84.0168,
    'Neptune': 164.79132
    }
    planets1 = planets.values()
    planets2 = planets.keys()
    list1 = list(planets1)
    list2 = list(planets2)
    if planet1 not in planets:
        return ()
    elif planet2 not in planets:
        return ()
    elif planet1 in list2 and planet2 in list2:
        for i in range(list1.index(planets[planet1]), list1.index(planets[planet2])+1):
            return tuple(list2[i])
    else:
        return ()
