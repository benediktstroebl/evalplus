
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
    # Check if the planets are valid
    if not is_planet(planet1) or not is_planet(planet2):
        return ()
    
    # Get the sun position
    sun_position = get_sun_position()
    
    # Get the positions of the planets
    planet1_position = get_planet_position(planet1, sun_position)
    planet2_position = get_planet_position(planet2, sun_position)
    
    # Get the positions of all planets located between the orbits of planet1 and planet2
    positions = get_planet_positions(planet1_position, planet2_position)
    
    # Sort the positions by the proximity to the sun
    sorted_positions = sorted(positions, key=lambda x: x[1])
    
    return tuple(sorted_positions)
