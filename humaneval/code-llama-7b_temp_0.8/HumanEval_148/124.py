
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

    list_planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planet1_index, planet2_index = None, None

    for i in range(len(list_planets)):
        if list_planets[i] == planet1:
            planet1_index = i
        elif list_planets[i] == planet2:
            planet2_index = i

    if planet1_index == None or planet2_index == None:
        return ()
    elif planet1_index < planet2_index:
        return list_planets[planet1_index+1:planet2_index]
    else:
        return list_planets[planet2_index+1:planet1_index]
