
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
    planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        
    if planet1 not in planet_names or planet2 not in planet_names:
        return tuple()
        
    planet_indices_1, planet_indices_2 = planet_names.index(planet1), planet_names.index(planet2)

    if planet_indices_1 < planet_indices_2:
        planet_one_orbit, planet_two_orbit = range(planet_indices_1, planet_indices_2 + 1), range(planet_indices_2 + 1, planet_indices_1 + 1)
    else:
        planet_one_orbit, planet_two_orbit = range(planet_indices_2, planet_indices_1 + 1), range(planet_indices_1 + 1, planet_indices_2 + 1)
        
    return tuple(planet_names[i] for i in planet_one_orbit), tuple(planet_names[i] for i in planet_two_orbit)

