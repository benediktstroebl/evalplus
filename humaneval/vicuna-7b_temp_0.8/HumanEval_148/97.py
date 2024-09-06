
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
    # check if the planet1 and planet2 are correct planet names
    if not is_correct_planet_name(planet1) or not is_correct_planet_name(planet2):
        return []
    
    # check if the orbit of the first planet is closer to the sun than the second planet
    if not is_closest_to_sun(planet1):
        return []
    
    # get all planets whose orbit is located between the orbit of planet1 and the orbit of planet2
    planet_list = get_planets_between(planet1, planet2)
    
    # sort the planet list by the proximity to the sun
    planet_list.sort(key=lambda x: (x.distance_to_sun(), x.name))
    
    return planet_list
