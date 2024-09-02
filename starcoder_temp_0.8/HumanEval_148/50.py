
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
    # Planet:
    #   1  mercury
    #   2  venus
    #   3  earth
    #   4  mars
    #   5  jupiter
    #   6  saturn
    #   7  uranus
    #   8  neptune
    
    planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planet_1 = planets_list.index(planet1)
    planet_2 = planets_list.index(planet2)
    bf_list = planets_list[planet_1:planet_2+1]
    bf_list.remove(planet1)
    bf_list.remove(planet2)
    return tuple(bf_list)
