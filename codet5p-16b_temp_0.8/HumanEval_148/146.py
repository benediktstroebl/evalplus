
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

    
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn",
    "Uranus", "Neptune")
    
    for i in planets:
        if i == planet1 or i == planet2:
            continue
        else:
            return ()
    
    if planet1 == "Mercury":
        if planet2 == "Venus":
            return ("Venus", "Earth")
        elif planet2 == "Earth":
            return ("Mercury", "Venus", "Mars")
        elif planet2 == "Mars":
            return ("Mercury", "Venus", "Earth", "Mars")
        elif planet2 == "Jupiter":
            return ("Mercury", "Venus", "Earth", "Mars", "Jupiter")
        elif planet2 == "Saturn":
            return ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn")
        elif planet2 == "Uranus":
            return ("Mercury", "Venus", "Earth", "Mars", "Jupiter
