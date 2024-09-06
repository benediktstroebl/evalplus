
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
    a = "Mercury"
    b = "Venus"
    c = "Earth"
    d = "Mars"
    e = "Jupiter"
    f = "Saturn"
    g = "Uranus"
    h = "Neptune"
    if planet1 != a and planet1 != b and planet1 != c and planet1 != d and planet1 != e and planet1 != f and planet1 != g and planet1 != h:
        return ()
    elif planet2 != a and planet2 != b and planet2 != c and planet2 != d and planet2 != e and planet2 != f and planet2 != g and planet2 != h:
        return ()
    if planet1 == a and planet2 == h:
        return (g,f,e,d,c,b)
    elif planet1 == a and planet2 == f:
        return (g,e,d,c,b)
    elif planet1 == a and planet2 == g:
        return (f,e,d,c,b)
    elif planet1 == a and planet2 == e
