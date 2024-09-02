
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
    planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planet_index1 = planet_list.index(planet1)
    planet_index2 = planet_list.index(planet2)
    result = []
    if planet1 in planet_list and planet2 in planet_list:
        for planet in planet_list:
            if planet_index1 < planet_index2:
                if planet_index1 < planet_list.index(planet) < planet_index2:
                    result.append(planet)
            else:
                if planet_index1 < planet_list.index(planet) or planet_index2 < planet_list.index(planet):
                    result.append(planet)
    return tuple(result)
