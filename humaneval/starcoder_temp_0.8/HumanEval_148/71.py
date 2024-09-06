
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
    planet1 = planet1.lower()
    planet2 = planet2.lower()
    if planet1 == "mercury":
        return ("venus")
    elif planet1 == "venus":
        return ("earth", "mars")
    elif planet1 == "earth":
        return ("mars", "jupiter")
    elif planet1 == "mars":
        return ("jupiter", "saturn")
    elif planet1 == "jupiter":
        return ("saturn", "uranus")
    elif planet1 == "saturn":
        return ("uranus", "neptune")
    elif planet1 == "uranus":
        return ("neptune")
    elif planet1 == "neptune":
        return ("")
    elif planet2 == "mercury":
        return ("venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune")
    elif planet2 == "venus":
        return ("earth", "mars", "jupiter", "saturn", "uranus", "neptune")
    elif planet2 == "earth":
        return ("mars", "jupiter", "saturn", "uranus", "neptune")
    elif planet2 == "mars":
        return ("jupiter", "saturn", "uranus", "neptune")
    elif planet2 == "jupiter":
        return ("saturn", "uranus", "neptune")
    elif planet2 == "saturn":
        return ("uranus", "neptune")
    elif planet2 == "uranus":
        return ("neptune")
    elif planet2 == "neptune":
        return ("")
    else:
        return ()
