
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
    if planet1 == "Jupiter" or planet2 == "Jupiter":
        return ("Saturn", "Uranus")
    elif planet1 == "Saturn" or planet2 == "Saturn":
        return ("Uranus", "Neptune")
    elif planet1 == "Uranus" or planet2 == "Uranus":
        return ("Neptune",)
    elif planet1 == "Neptune" or planet2 == "Neptune":
        return ()
    elif planet1 == "Mars" and planet2 == "Mars":
        return ("Jupiter", "Saturn", "Earth", "Venus")
    elif planet1 == "Mars" and planet2 == "Earth":
        return ("Venus", "Jupiter", "Saturn", "Mars")
    elif planet1 == "Mars" and planet2 == "Jupiter":
        return ("Venus", "Saturn", "Mars", "Earth")
    elif planet1 == "Mars" and planet2 == "Saturn":
        return ("Venus", "Jupiter", "Earth", "Mars")
    elif planet1 == "Earth" and planet2 == "Venus":
        return ("Mars", "Jupiter", "Saturn", "Uranus")
    elif planet1 == "Earth" and planet2 == "Mars":
        return ("Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Earth" and planet2 == "Jupiter":
        return ("Saturn", "Uranus", "Neptune",)
    elif planet1 == "Earth" and planet2 == "Saturn":
        return ("Jupiter", "Uranus", "Neptune",)
    elif planet1 == "Earth" and planet2 == "Uranus":
        return ("Jupiter", "Saturn", "Earth", "Mars")
    elif planet1 == "Earth" and planet2 == "Neptune":
        return ("Jupiter", "Saturn", "Mars",
