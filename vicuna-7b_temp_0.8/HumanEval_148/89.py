
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
    if not planet1.lower() in ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]:
        return ()
    if not planet2.lower() in ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]:
        return ()

    a = (planet1, planet2)
    b = (planet2, planet1)
    c = (planet1, planet2)
    d = (planet2, planet1)
    sorted_tuple = sorted((a, b, c, d), key=lambda x: (a_c(x[0], x[1]), a_b(x[0], x[1])))
    return sorted_tuple
