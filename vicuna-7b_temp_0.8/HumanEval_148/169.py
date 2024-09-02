
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
    # Check if the input planets are valid
    if not isinstance(planet1, str) or not isinstance(planet2, str):
        return ()
    
    # Get the list of valid planets
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # Get the orbits of the two planets
    planet1_semi_major_axis = get_semi_major_axis(planet1)
    planet2_semi_major_axis = get_semi_major_axis(planet2)
    
    # Find the range of orbits between the two planets
    min_semi_major_axis = min(planet1_semi_major_axis, planet2_semi_major_axis)
    max_semi_major_axis = max(planet1_semi_major_axis, planet2_semi_major_axis)
    
    # Get the sorted list of planets based on their semi-major axes
    planet_list = sorted(planets, key=lambda x: x.get_semi_major_axis())
    
    # Return the list of planets in order of proximity to the sun
    return [p for p in planet_list if p.get_semi_major_axis() > min_semi_major_axis and p.get_semi_major_axis() < max_semi_major_axis]
