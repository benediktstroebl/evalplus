
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
    planet_dict = {"Mercury":1, "Venus":2, "Earth":3, "Mars":4, "Jupiter":5, "Saturn":6, "Uranus":7, "Neptune":8}
    result = []
    if (planet1 in planet_dict and planet2 in planet_dict):
        if planet1 == planet2:
            return ()
        if planet_dict[planet1] < planet_dict[planet2]:
            for i in range(planet_dict[planet1] + 1, planet_dict[planet2]):
                result.append(list(planet_dict.keys())[i])
        else:
            for i in range(planet_dict[planet2] + 1, planet_dict[planet1]):
                result.append(list(planet_dict.keys())[i])
    return tuple(result)
    
