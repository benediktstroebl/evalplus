
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
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # Check for correct planet name
    if (planet1 not in planets):
        return ()
    elif (planet2 not in planets):
        return ()
    
    # Convert planet names to planets' indexes
    planet1 = planets.index(planet1)
    planet2 = planets.index(planet2)
    
    # Check if planet1 is before or after planet2
    if planet1 < planet2:
        # Slice the planet list between planet1 and planet2 indexes
        return tuple(planets[planet1 + 1: planet2])
    else:
        # Slice the planet list between planet2 and planet1 indexes
        return tuple(planets[planet2 + 1: planet1])
    
