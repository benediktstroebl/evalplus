
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
    # check that the planet names are valid
    if not planet1 or not planet2:
        return ()
    if planet1 == "Mercury" and planet2 == "Mercury":
        return ()
    elif planet1 == "Jupiter" and planet2 == "Jupiter":
        return ()
    elif planet1 in ["Mercury", "Venus", "Earth", "Mars", "Saturn", "Uranus", "Neptune"] and planet2 in ["Mercury", "Venus", "Earth", "Mars", "Saturn", "Uranus", "Neptune"]:
        return [planet for planet in sorted(range(len(planet1)), key=lambda i: ((i+planet1.index(planet2))/3.0 - 1.0)) if planet in range(len(planet1))]
    else:
        return ()
