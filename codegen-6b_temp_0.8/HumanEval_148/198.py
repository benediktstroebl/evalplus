
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
    planetlist = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 in planetlist and planet2 in planetlist:
        planet1 = planetlist[planetlist.index(planet1)]
        planet2 = planetlist[planetlist.index(planet2)]
        planets_in_range = []
        for planet in planetlist:
            if (planet1 in list(orbit(planet)) or planet1 == planet) and (planet2 in list(orbit(planet)) or planet2 == planet):
                planets_in_range.append(planet)
        planets_in_range.sort(key = lambda planet : orbit(planet)[0])
        return tuple(planets_in_range)
    else:
        return tuple()
