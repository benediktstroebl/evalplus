
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
    # Check if planets are correct
    if planet1 not in ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']:
        return []
    if planet2 not in ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']:
        return []
    
    # Calculate the orbit of each planet
    planet1_orbit = get_orbit(planet1)
    planet2_orbit = get_orbit(planet2)
    
    # Calculate the distances of the other planets from the sun
    other_planets = [get_orbit(p) for p in list(planet1_orbit.keys()) if p not in [planet1_orbit[p] for p in planet1_orbit.keys()]]
    distances = [planet1_orbit[p] - planet2_orbit for p in other_planets]
    distances.sort()
    
    # Get the indices of the planets
    planet_indices = [i for i, d in enumerate(distances) if d < (planet2_orbit[i] - planet1_orbit[i])]
    planets = [planet1_orbit[i] for i in planet_indices]
    
    return planets
