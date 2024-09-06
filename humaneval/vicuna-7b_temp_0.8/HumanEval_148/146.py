
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
    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    if planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    
    # Get the orbit of the first planet
    planet1_orbit = get_orbit(planet1)
    
    # Get the orbit of the second planet
    planet2_orbit = get_orbit(planet2)
    
    # Get the orbit of the third planet
    planet3_orbit = get_orbit(planet1)
    
    # Get the orbit of the fourth planet
    planet4_orbit = get_orbit(planet2)
    
    # Find the closest planet to the Sun
    closest_planet = planet1_orbit
    
    # Iterate through all planets
    for planet in planet1_orbit, planet2_orbit, planet3_orbit, planet4_orbit:
        # Check if the planet's orbit is between the orbits of the first two planets
        if planet < closest_planet:
            closest_planet = planet
    
    # Sort the planets by proximity to the sun
    sorted_planets = sorted((closest_planet,), key=lambda x: x.distance_to_sun)
    
    return tuple(sorted_planets)
