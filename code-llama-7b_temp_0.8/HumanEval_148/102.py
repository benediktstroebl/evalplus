
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

    if planet1 not in planet_list or planet2 not in planet_list:
        return ()
    else:
        if planet1 == "Earth":
            return planet_list[:2]
        elif planet2 == "Mercury":
            return planet_list[-2:]
        else:
            if planet1 == "Mercury":
                index1 = 0
            else:
                index1 = planet_list.index(planet1)
            if planet2 == "Uranus":
                index2 = 6
            else:
                index2 = planet_list.index(planet2)
            if index1 < index2:
                return planet_list[index1 + 1: index2]
            else:
                return planet_list[index1 + 1: 7] + planet_list[:index2 + 1]
