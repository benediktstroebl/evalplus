
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
    def bf_loop(planet1, planet2):
        if planet1 not in ["Jupiter", "Saturn", "Uranus", "Neptune", "Earth", "Mercury", "Venus", "Mars"]:
            return ()
        elif planet2 not in ["Jupiter", "Saturn", "Uranus", "Neptune", "Earth", "Mercury", "Venus", "Mars"]:
            return ()
        else:
            return planet1, planet2

    return sorted(list(bf_loop(planet1, planet2)), key=lambda x: planet.sun_distance(x))
