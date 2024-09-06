
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
    if not validate_planet_names(planet1, planet2):
        return ()
    
    # Sort the planets by their proximity to the sun
    sorted_planets = sorted((p.semi_major_axis, p.mean_distance_to_the_sun) for p in planet1.planets if p != planet1 and p != planet2)
    
    # Create an empty list to store the sorted planets
    planets = []
    
    # Add the planets to the list in order
    for (a, d) in sorted_planets:
        planets.append((a, d))
    
    return planets
