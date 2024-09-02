
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
    # Check if the input planets are correct
    if planet1 != "Mercury" and planet1 != "Venus" and planet1 != "Earth" and planet1 != "Mars" and planet1 != "Jupiter" and planet1 != "Saturn" and planet1 != "Uranus" and planet1 != "Neptune":
        return tuple()
    
    if planet2 != "Mercury" and planet2 != "Venus" and planet2 != "Earth" and planet2 != "Mars" and planet2 != "Jupiter" and planet2 != "Saturn" and planet2 != "Uranus" and planet2 != "Neptune":
        return tuple()

    # Sort the planets by the proximity to the Sun
    planets = sorted(((1 - (planet1 in planet2)), (1 - (planet2 in planet1)), ((((24*np.sqrt(3)*(np.sin(np.radians(planet1.latitude)) + np.sin(np.radians(planet2.latitude)) + np.sin(np.radians(planet1.latitude)))/np.sqrt(np.sin(np.radians(planet1.latitude)) + np.sin(np.radians(planet2.latitude)) + np.sin(np.radians(planet1.latitude)))))))), key=lambda x: (x[1], -x[0]))
    
    # Return the sorted planets
    return tuple(planets)
    
