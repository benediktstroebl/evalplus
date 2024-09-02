
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
    planet1_index = 0
    planet2_index = 0
    if planet1 not in solar_system.keys():
        return ()
    if planet2 not in solar_system.keys():
        return ()
    for key in solar_system.keys():
        if key == planet1:
            planet1_index = solar_system[key]
        if key == planet2:
            planet2_index = solar_system[key]
    planet_list = []
    for key in solar_system.keys():
        if planet1_index < solar_system[key] < planet2_index:
            planet_list.append(key)
    return tuple(planet_list)

    "Mercury": 0.39,
    "Venus": 0.72,
    "Earth": 1.00,
    "Mars": 1.52,
    "Jupiter": 5.20,
    "Saturn": 9.54,
    "Uranus": 19.1
