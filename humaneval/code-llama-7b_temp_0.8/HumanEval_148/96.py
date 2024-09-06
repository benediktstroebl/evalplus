
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
    if planet1 in ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn"):
        if planet2 in ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn"):
            if planet1 != planet2:
                if (planet1 == "Mercury" and planet2 != "Venus") or (planet1 == "Venus" and planet2 != "Earth") or (planet1 == "Earth" and planet2 != "Mars") or (planet1 == "Mars" and planet2 != "Jupiter") or (planet1 == "Jupiter" and planet2 != "Saturn"):
                    return (planet1, planet2)
                elif (planet2 == "Mercury" and planet1 != "Venus") or (planet2 == "Venus" and planet1 != "Earth") or (planet2 == "Earth" and planet1 != "Mars") or (planet2 == "Mars" and planet1 != "Jupiter") or (planet2 == "Jupiter" and planet1 != "Saturn"):
                    return (planet2, planet1)
                else:
                    return ()
            else:
                return ()
        else:
            return ()
    else:
        return ()

