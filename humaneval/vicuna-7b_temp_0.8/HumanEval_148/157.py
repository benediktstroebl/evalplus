
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
    # Validate input
    if not is_planet_name(planet1) or not is_planet_name(planet2):
        return ()
    
    # Get the list of planets and their orbits
    orbits = []
    for planet in planets:
        orbits.append(planet.orbit)
    
    # Filter the orbits to get the ones between the orbits of planet1 and planet2
    filtered_orbits = [orbit for orbit in orbits if orbit.planet in (planet1, planet2)]
    
    # Sort the filtered orbits by proximity to the sun
    sorted_orbits = sorted(filtered_orbits, key=lambda orbit: orbit.distance_to_sun)
    
    # Join the sorted orbits into a single string
    result = ', '.join(str(orbit.planet) for orbit in sorted_orbits)
    
    return result.split(', ')
