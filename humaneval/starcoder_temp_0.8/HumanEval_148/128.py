
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
    if planet1 == "Mercury":
        ind1 = 0
    elif planet1 == "Venus":
        ind1 = 1
    elif planet1 == "Earth":
        ind1 = 2
    elif planet1 == "Mars":
        ind1 = 3
    elif planet1 == "Jupiter":
        ind1 = 4
    elif planet1 == "Saturn":
        ind1 = 5
    elif planet1 == "Uranus":
        ind1 = 6
    elif planet1 == "Neptune":
        ind1 = 7
    else:
        return ()

    if planet2 == "Mercury":
        ind2 = 0
    elif planet2 == "Venus":
        ind2 = 1
    elif planet2 == "Earth":
        ind2 = 2
    elif planet2 == "Mars":
        ind2 = 3
    elif planet2 == "Jupiter":
        ind2 = 4
    elif planet2 == "Saturn":
        ind2 = 5
    elif planet2 == "Uranus":
        ind2 = 6
    elif planet2 == "Neptune":
        ind2 = 7
    else:
        return ()

    return tuple(solar_system[i] for i in range(ind1+1, ind2))
