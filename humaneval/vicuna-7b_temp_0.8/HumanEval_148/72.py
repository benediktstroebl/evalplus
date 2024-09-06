
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
    if planet1 == "Jupiter" or planet1 == "Saturn" or planet1 == "Uranus" or planet1 == "Neptune" or planet2 == "Jupiter" or planet2 == "Saturn" or planet2 == "Uranus" or planet2 == "Neptune":
        return ()
    elif planet1 < "Mercury" and planet2 > "Mercury":
        return (planet1, planet2)
    elif planet1 > "Mercury" and planet2 < "Mercury":
        return (planet2, planet1)
    else:
        if "Mars" <= planet1 <= "Saturn" and "Jupiter" <= planet2 <= "Neptune":
            return (planet1, planet2)
        elif "Venus" <= planet1 <= "Mercury" and "Mars" <= planet2 <= "Jupiter":
            return (planet1, planet2)
        else:
            return ()
