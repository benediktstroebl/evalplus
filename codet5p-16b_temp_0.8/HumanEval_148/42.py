
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

    assert planet1 == "Mercury" or planet1 == "Venus" or planet1 == "Earth"
    assert planet2 == "Mercury" or planet2 == "Venus" or planet2 == "Earth"
    assert planet1!= planet2
    if planet1 == 'Mercury':
        planets = ("Venus", "Earth", "Mars")
    elif planet1 == 'Venus':
        planets = ("Mercury", "Earth", "Mars")
    elif planet1 == 'Earth':
        planets = ("Mercury", "Venus", "Mars")
    if planet2 == 'Mercury':
        planets = ("Venus", "Earth", "Mars")
    elif planet2 == 'Venus':
        planets = ("Mercury", "Earth", "Mars")
    elif planet2 == 'Earth':
        planets = ("Mercury", "Venus", "Mars")
    return planets


