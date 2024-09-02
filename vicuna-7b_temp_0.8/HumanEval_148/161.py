
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
    # Determine the position of the two planets in the solar system
    planet1_position = get_distance(planet1, "sun")
    planet2_position = get_distance(planet2, "sun")
    
    # Determine the position of all other planets in the solar system
    other_planets = []
    for planet in planets:
        other_planets.append(get_distance(planet, "sun"))
    
    # Sort the list of planets based on proximity to the sun
    planets_sorted = sorted(other_planets, key=lambda x: x - planet1_position)
    
    # Return the planets in the sorted list
    return planets_sorted[planet2_position - planet1_position:]
