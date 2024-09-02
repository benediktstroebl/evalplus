
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
    if planet1 == "Mercury" or planet2 == "Mercury":
        if planet1 == "Mercury":
            planet1 = "Venus"
        elif planet2 == "Mercury":
            planet2 = "Venus"
        else:
            pass
    if planet1 == "Venus" or planet2 == "Venus":
        if planet1 == "Venus":
            planet1 = "Earth"
        elif planet2 == "Venus":
            planet2 = "Earth"
        else:
            pass
    if planet1 == "Earth" or planet2 == "Earth":
        if planet1 == "Earth":
            planet1 = "Mars"
        elif planet2 == "Earth":
            planet2 = "Mars"
        else:
            pass
    if planet1 == "Mars" or planet2 == "Mars":
        if planet1 == "Mars":
            planet1 = "Jupiter"
        elif planet2 == "Mars":
            planet2 = "Jupiter"
        else:
           
