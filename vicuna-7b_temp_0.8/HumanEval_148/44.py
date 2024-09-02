
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
    # Get the distance between the two planets
    distance = get_distance(planet1, planet2)
    
    # Create a list of the planets
    planets = [planet1, planet2]
    planets.extend(range(1, 10))
    
    # Sort the planets by distance from the sun
    planets.sort(key=lambda x: abs(x.a - distance))
    
    # Get the first two planets whose orbits are located between the orbit of planet1 and the orbit of planet2
    orbit_range = get_orbit_range(planet1, planet2)
    return tuple(planets[i:j] for i, j in zip(range(len(planets)), orbit_range))
