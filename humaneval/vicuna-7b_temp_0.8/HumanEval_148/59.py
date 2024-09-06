
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
    # First, check that the input planets are valid
    if planet1 == "Mercury" or planet1 == "Venus" or planet1 == "Earth" or \
       planet1 == "Mars" or planet1 == "Jupiter" or planet1 == "Saturn" or \
       planet1 == "Uranus" or planet1 == "Neptune":
        return ()
    if planet2 == "Mercury" or planet2 == "Venus" or planet2 == "Earth" or \
       planet2 == "Mars" or planet2 == "Jupiter" or planet2 == "Saturn" or \
       planet2 == "Uranus" or planet2 == "Neptune":
        return ()
    
    # Then, check the orbit of each planet and the distance between the orbits
    distance = 0
    for planet in planet1, planet2:
        distance += (planet.get_distance_to_sun() - 0.0)**2
    
    # Sort the planets by their proximity to the sun
    planets = sorted(range(len(planet1)), key=lambda x: x - distance)
    
    return planets
