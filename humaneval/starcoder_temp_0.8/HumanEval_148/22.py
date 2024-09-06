
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
        index1 = 0
    elif planet1 == "Venus":
        index1 = 1
    elif planet1 == "Earth":
        index1 = 2
    elif planet1 == "Mars":
        index1 = 3
    elif planet1 == "Jupiter":
        index1 = 4
    elif planet1 == "Saturn":
        index1 = 5
    elif planet1 == "Uranus":
        index1 = 6
    elif planet1 == "Neptune":
        index1 = 7
    else:
        return ()

    if planet2 == "Mercury":
        index2 = 0
    elif planet2 == "Venus":
        index2 = 1
    elif planet2 == "Earth":
        index2 = 2
    elif planet2 == "Mars":
        index2 = 3
    elif planet2 == "Jupiter":
        index2 = 4
    elif planet2 == "Saturn":
        index2 = 5
    elif planet2 == "Uranus":
        index2 = 6
    elif planet2 == "Neptune":
        index2 = 7
    else:
        return ()

    if index1 <= index2:
        return tuple(sorted(planets[index1:index2 + 1]))
    else:
        return tuple(sorted(planets[index1:] + planets[:index2 + 1]))
