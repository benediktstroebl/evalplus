
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
    
    list_planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    list_planets_index = [0, 1, 2, 3, 4, 5, 6, 7]
    planet1_index = list_planets.index(planet1)
    planet2_index = list_planets.index(planet2)
    
    list_in_between = []
    if planet1_index < planet2_index:
        for i in range(planet1_index, planet2_index+1):
            list_in_between.append(list_planets[i])
    else:
        for i in range(planet2_index, planet1_index+1):
            list_in_between.append(list_planets[i])

    return tuple(list_in_between)
