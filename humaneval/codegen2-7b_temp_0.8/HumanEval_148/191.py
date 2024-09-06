
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
    planet1 = planet1.strip().capitalize()
    planet2 = planet2.strip().capitalize()
    list1 = []
    list2 = []
    if planet1 in PLANETS and planet2 in PLANETS:
        for i in range(len(ORB_PLANETS)):
            if planet1 in ORB_PLANETS[i] and planet2 in ORB_PLANETS[i]:
                list1.append(i)
                list2.append(i)
    if len(list1) == 0:
        return tuple()
    else:
        return tuple(sorted(list1)[0:5], sorted(list2)[0:
