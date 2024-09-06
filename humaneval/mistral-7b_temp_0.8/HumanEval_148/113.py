
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
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 in planets and planet2 in planets:
        if planet1 in ["Mercury", "Venus"] and planet2 in ["Venus", "Earth"]:
            return ("Venus",)
        elif planet1 in ["Venus", "Earth"] and planet2 in ["Earth", "Mars"]:
            return ("Earth",)
        elif planet1 in ["Earth", "Mars"] and planet2 in ["Mars", "Jupiter"]:
            return ("Mars",)
        elif planet1 in ["Mars", "Jupiter"] and planet2 in ["Jupiter", "Saturn"]:
            return ("Jupiter",)
        elif planet1 in ["Jupiter", "Saturn"] and planet2 in ["Saturn", "Uranus"]:
            return ("Saturn",)
        elif planet1 in ["Saturn", "Uranus"] and planet2 in
