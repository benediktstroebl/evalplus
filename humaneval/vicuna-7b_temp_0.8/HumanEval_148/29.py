
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
    if planet1.lower() not in ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]:
        return ()
    if planet2.lower() not in ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]:
        return ()
    
    # Check if the planets are in the correct order
    if planet1.lower() < planet2.lower():
        # Sort the list of planets by their proximity to the sun
        planets = [(sun_to_planet(planet) for planet in sorted((sun_to_planet(planet),)))]
    else:
        planets = [(sun_to_planet(planet) for planet in (sun_to_planet(planet2), sun_to_planet(planet1)))]
    
    # Return the list of planets whose orbits are between the two
    return tuple(planets[i:j]) for i, j in zip((sun_to_planet(planet1), sun_to_planet(planet2)), (sun_to_planet(planet1), sun_to_planet(planet2)))
