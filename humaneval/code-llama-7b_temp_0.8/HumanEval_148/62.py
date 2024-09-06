
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
    
    planet = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planet_dic = {"Mercury": 0, "Venus": 1, "Earth": 2, "Mars": 3, "Jupiter": 4, "Saturn": 5, "Uranus": 6, "Neptune": 7}
    min_index = min(planet_dic[planet1], planet_dic[planet2])
    max_index = max(planet_dic[planet1], planet_dic[planet2])
    res = []
    
    for i in range(min_index+1, max_index):
        res.append(planet[i])
        
    return tuple(res)
