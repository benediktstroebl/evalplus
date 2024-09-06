
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
    # Input validation
    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter",
                       "Saturn", "Uranus", "Neptune"]:
        return ()
    if planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter",
                       "Saturn", "Uranus", "Neptune"]:
        return ()
    # Tuple with all planets in the solar system
    solarsystem = ("Mercury", "Venus", "Earth", "Mars", "Jupiter",
                   "Saturn", "Uranus", "Neptune")
    # List for storing planets between planet1 and planet2
    planets = []
    # Check if planet1 and planet2 are neighbours
    if planet1 == "Mercury" and planet2 == "Venus" or planet1 == "Venus" and 
       planet2 == "Earth" or planet1 == "Earth" and planet2 == "Mars" or 
       planet1
