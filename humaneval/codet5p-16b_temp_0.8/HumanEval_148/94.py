
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

    planets = {"Mercury": ["Venus", "Earth", "Mars"], 
                "Venus": ["Earth", "Mars", "Jupiter", "Saturn"], 
                "Earth": ["Mercury", "Mars", "Jupiter", "Saturn"], 
                "Mars": ["Mercury", "Earth", "Jupiter", "Saturn"], 
                "Jupiter": ["Venus", "Earth", "Mars", "Saturn"], 
                "Saturn": ["Uranus", "Neptune", "Jupiter", "Earth", "Mars"], 
                "Uranus": ["Neptune", "Earth", "Mars", "Jupiter", "Saturn"], 
                "Neptune": ["Jupiter", "Uranus", "Earth", "Mars", "Saturn"]}
    
    if planet1 not in planets:
        return ()
    if planet2 not in planets:
        return ()
    
    visited = set()
    to_visit = [planet1]
    while len(to_visit) > 0:
        cur_planet = to_visit.
