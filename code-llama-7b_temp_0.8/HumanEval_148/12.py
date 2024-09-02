
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
    if planet1 not in ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"):
        return ()
    if planet2 not in ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"):
        return ()
    if planet1 in ("Mercury", "Venus", "Earth"):
        if planet1 == planet2:
            return ()
        elif planet1 == "Mercury" and planet2 == "Venus":
            return ("Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
        elif planet1 == "Mercury" and planet2 == "Earth":
            return ("Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
        elif planet1 == "Venus" and planet2 == "Earth":
            return ("Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
        else:
            return ("Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 == "Mars" and planet2 == "Jupiter":
        return ("Saturn", "Uranus", "Neptune")
    elif planet1 == "Jupiter" and planet2 == "Saturn":
        return ("Uranus", "Neptune")
    elif planet1 == "Saturn" and planet2 == "Uranus":
        return ("Neptune",)
    else:
        return ()
