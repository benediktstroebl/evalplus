
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
    # Create a list of all the planets
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # Check if the planets are valid
    if planet1 not in planets:
        return ()
    if planet2 not in planets:
        return ()
    
    # Check if the planets are in the correct order
    if planet1 < planet2 and planet1 not in [planet2, "Sun"]:
        return planets[planet1:planet2]
    if planet1 > planet2 and planet1 not in [planet2, "Sun"]:
        return planets[planet2:planet1]
    
    # Sort the list of planets by proximity to the sun
    sorted_planets = sorted(planets, key=lambda x: (x.distance, x.name))
    
    # Return the list of planets between the two specified planets
    return sorted_planets[planet1:planet2]
