
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
    planet_name = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", 
                    "Saturn", "Uranus", "Neptune")
    planet_order = (1, 2, 3, 4, 5, 6, 7, 8)
    order_dict = dict(zip(planet_name, planet_order))
    
    if planet1 not in planet_name or planet2 not in planet_name:
        return ()

    if order_dict[planet1] < order_dict[planet2]:
        planet_range = list(planet_name[order_dict[planet1]: order_dict[planet2]+1])
    elif order_dict[planet1] > order_dict[planet2]:
        planet_range = list(planet_name[order_dict[planet2]: order_dict[planet1]+1])
    else:
        return planet_name[order_dict[planet1]: order_dict[planet2]+1]
    
    return tuple(planet_range[planet_range.index(planet1) : planet_range.index(planet2)+1])
    
    
    
    
    
