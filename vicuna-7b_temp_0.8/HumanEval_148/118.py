
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
    # Create a list of all planets
    all_planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # Check if the input is valid
    if not planet1 in all_planets:
        return []
    if not planet2 in all_planets:
        return []
    
    # Find the orbit of each planet
    planet_orbits = [planet.orbit for planet in all_planets]
    
    # Find the distance between the orbits
    distance = abs(planet1.orbit[0] - planet2.orbit[0])
    
    # Find the indices of the planets in the sorted order
    planet_indices = np.argsort(distance)[1:]
    
    # Return the sorted planets
    return all_planets[planet_indices]
