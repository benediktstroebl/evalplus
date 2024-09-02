
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
    if planet1 not in ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune") or planet2 not in ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"):
        return ()
    if planet1 == planet2:
        return ()
    
    if planet1 == "Mercury":
        if planet2 == "Venus":
            return ("Venus",)
        else:
            return ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Venus":
        if planet2 == "Earth":
            return ("Earth",)
        else:
            return ("Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Earth":
        if planet2 == "Mars":
            return ("Mars",)
        else:
            return ("Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Mars":
        if planet2 == "Jupiter":
            return ("Jupiter",)
        else:
            return ("Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Jupiter":
        if planet2 == "Saturn":
            return ("Saturn",)
        else:
            return ("Saturn", "Uranus", "Neptune")
    elif planet1 == "Saturn":
        if planet2 == "Uranus":
            return ("Uranus",)
        else:
            return ("Uranus", "Neptune")
    elif planet1 == "Uranus":
        if planet2 == "Neptune":
            return ("Neptune",)
        else:
            return ()
    else:
        return ()
