
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
    if planet1 not in solar_system:
        return tuple()
    if planet2 not in solar_system:
        return tuple()
        
    planet1_orbit = solar_system[planet1]
    planet2_orbit = solar_system[planet2]
    
    planet_between = tuple()
    for planet in solar_system:
        if planet not in (planet1, planet2):
            if solar_system[planet] >= planet1_orbit and \
                solar_system[planet] <= planet2_orbit:
                planet_between += (planet,)
    return planet_between
