
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
    if planet1 == "Jupiter" or planet1 == "Saturn" or planet1 == "Uranus":
        if planet2 == "Jupiter" or planet2 == "Saturn" or planet2 == "Uranus":
            return (("Jupiter", "Saturn", "Uranus"),)
        elif planet2 == "Sun":
            return (("Mars", "Venus", "Mercury", "Earth"),)
        elif planet2 == "Venus":
            return (("Mars", "Venus", "Mercury", "Earth"),)
        elif planet2 == "Mars":
            return (("Venus", "Mercury", "Earth", "Mars"),)
        elif planet2 == "Venus":
            return (("Mercury", "Mars", "Earth", "Jupiter", "Saturn"),)
        elif planet2 == "Mars":
            return (("Mercury", "Jupiter", "Saturn", "Uranus"),)
        elif planet2 == "Sun":
            return (("Jupiter", "Saturn", "Uranus",),)
        else:
            return ()
    elif planet1 == "Earth":
        if planet2 == "Venus":
            return (("Mercury", "Venus", "Earth"),)
        elif planet2 == "Mars":
            return (("Venus", "Earth", "Mars"),)
        elif planet2 == "Jupiter":
            return (("Saturn", "Earth", "Jupiter"),)
        elif planet2 == "Saturn":
            return (("Earth", "Jupiter", "Saturn"),)
        elif planet2 == "Uranus":
            return (("Earth", "Jupiter", "Saturn", "Uranus"),)
        else:
            return ()
    elif planet1 == "Mars":
        if planet2 == "Jupiter":
            return (("Saturn", "Earth", "Mars", "Jupiter"),)
        elif planet2 == "
