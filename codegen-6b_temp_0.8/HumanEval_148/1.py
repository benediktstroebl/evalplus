
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
    # Make the dictionaries of the indexes of the planets and their names
    planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planets_dict1 = dict(zip(planets_list, range(0,8)))
    planets_dict2 = dict(zip(planets_list, range(1,9)))
    # Make the lists of the indexes of the orbit
    o1 = planets_dict1[planet1]
    o2 = planets_dict1[planet2]
    # Make the list of planets bifurcating
    list_bifurcation = []
    for index in range(o1+1, o2):
        list_bifurcation.append(planets_list[index])
    # Make the list of the other planets
    list_not_bifurcation = list(set(planets_list)-set(list_bifurcation))
    
    #return the list of planets bifurcating
    return tuple(list_bifurcation)
