
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
    planets = {
        "Mercury" : 57909227,
        "Venus" : 108208003,
        "Earth" : 149600000,
        "Mars" : 227943829,
        "Jupiter" : 778368799,
        "Saturn" : 1433536743,
        "Uranus" : 2872488287,
        "Neptune" : 4504468740
    }
    
    try:
        planet1_distance = planets[planet1]
        planet2_distance = planets[planet2]
    except KeyError:
        return ()
    
    sorted_planets = {k:v for k,v in planets.items() if planet1_distance < v < planet2_distance}
    sorted_planets = sorted(sorted_planets, key = lambda x: sorted_planets[x])
    
    return tuple(sorted_planets)
    
