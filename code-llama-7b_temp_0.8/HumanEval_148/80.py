
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
    # create a list with all planets
    planet_list = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    # create a list that will be returned by the function
    temp_list = []
    # add the name of the planets that are not planet1 or planet2 to the list
    # if they are closer to planet1 than planet2
    for planet in planet_list:
        if planet != planet1 and planet != planet2:
            if planet_list.index(planet1) < planet_list.index(planet):
                temp_list.append(planet)
    # add the name of the planets that are not planet1 or planet2 to the list
    # if they are closer to planet2 than planet1
    for planet in planet_list:
        if planet != planet1 and planet != planet2:
            if planet_list.index(planet2) < planet_list.index(planet):
                temp_list.append(planet)
    # delete the duplicates from the list
    return list(set(temp_list))

