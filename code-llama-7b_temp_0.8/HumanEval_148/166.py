
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
    if planet1 in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"] and planet2 in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        if "Mercury" in planet1 and "Mercury" in planet2:
            return ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
        if "Venus" in planet1 and "Venus" in planet2:
            return ("Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
        if "Earth" in planet1 and "Earth" in planet2:
            return ("Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
        if "Mars" in planet1 and "Mars" in planet2:
            return ("Jupiter", "Saturn", "Uranus", "Neptune")
        if "Jupiter" in planet1 and "Jupiter" in planet2:
            return ("Saturn", "Uranus", "Neptune")
        if "Saturn" in planet1 and "Saturn" in planet2:
            return ("Uranus", "Neptune")
        if "Uranus" in planet1 and "Uranus" in planet2:
            return ("Neptune",)
        if "Neptune" in planet1 and "Neptune" in planet2:
            return ()
    else:
        return ()
    

