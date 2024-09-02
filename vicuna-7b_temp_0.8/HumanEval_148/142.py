
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
    if not isinstance(planet1, str) or not isinstance(planet2, str):
        return ()
    if planet1 == "Mercury" or planet1 == "Venus" or planet1 == "Mars" or planet1 == "Jupiter" or planet1 == "Saturn" or planet1 == "Uranus" or planet1 == "Neptune":
        return ()
    if planet2 == "Mercury" or planet2 == "Venus" or planet2 == "Mars" or planet2 == "Jupiter" or planet2 == "Saturn" or planet2 == "Uranus" or planet2 == "Neptune":
        return ()
    if planet1 > "Mercury" and planet1 < "Saturn":
        if planet2 > "Mercury" and planet2 < "Saturn":
            return sorted(range(planet1, "Saturn"), key=lambda i: abs(i - Sun - Earth))
        else:
            return sorted(range(planet1, "Saturn"), key=lambda i: abs(i - Sun - Earth)) + sorted(range(planet2, "Saturn"), key=lambda i: abs(i - Sun - Earth))
    elif planet1 > "Saturn" and planet1 < "Uranus":
        if planet2 > "Saturn" and planet2 < "Uranus":
            return sorted(range(planet1, "Uranus"), key=lambda i: abs(i - Sun - Earth))
        else:
            return sorted(range(planet1, "Uranus"), key=lambda i: abs(i - Sun - Earth)) + sorted(range(planet2, "Uranus"), key=lambda i: abs(i - Sun - Earth))
    elif planet1 > "Uranus" and planet1 < "Neptune":
        return sorted(range(planet1, "Neptune"), key=lambda i: abs(i - Sun - Earth))
    else:
        return ()
