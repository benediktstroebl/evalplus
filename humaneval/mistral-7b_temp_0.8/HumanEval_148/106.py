
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
    # return []
    return_list = []
    start = 0
    if planet1 != "Mercury" or planet2 != "Neptune":
        return_list = []
    if planet1 == "Mercury":
        start = 1
        return_list.append("Venus")
    if planet1 == "Venus":
        start = 2
        return_list.append("Earth")
    if planet1 == "Earth":
        start = 3
        return_list.append("Mars")
    if planet1 == "Mars":
        start = 4
        return_list.append("Jupiter")
    if planet1 == "Jupiter":
        start = 5
        return_list.append("Saturn")
    if planet1 == "Saturn":
        start = 6
        return_list.append("Uranus")
    if planet1 == "Uranus":
        start = 7
        return_list.append("Neptune")
    if planet1 == "Neptune":
        start = 8
