
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
    if not isinstance(planet1,str) or not isinstance(planet2,str):
        return tuple()
    if planet1.lower() < planet2.lower():
        planet1, planet2 = planet2, planet1
    if planet1 in ("mercury","mars","earth","venus","jupiter","saturn","uranus","neptune"):
        return bf(planet1, planet2) + bf(planet2, planet1)
    if planet1 in ("uranus","neptune"):
        return bf(planet2, planet1) + bf(planet1, planet2)
    else:
        return tuple()

example = bf("Venus", "Mercury")
