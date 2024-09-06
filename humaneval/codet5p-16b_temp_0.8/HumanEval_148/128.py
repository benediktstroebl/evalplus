
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

    if planet1 == "" or planet2 == "":
        return []
    planet_names = {"Mercury": 0, "Venus": 1, "Earth": 2, "Mars": 3, 
                    "Jupiter": 4, "Saturn": 5, "Uranus": 6, "Neptune": 7}
    planet_values = [(1,2,3,4), (2,3,4,5), (3,4,5,6), (4,5,6,7), (5,6,7,8), 
                    (6,7,8,9), (7,8,9,10), (8,9,10,11)]
    for i in range(len(planet_names)):
        if planet1 == list(planet_names)[i]:
            planet1_val = planet_values[i]
        if planet2 == list(planet_names)[i]:
            planet2_val = planet_values[i]
    final_list = []
    for i in planet1_val:
        if i in planet2_val:
            final_list.append
