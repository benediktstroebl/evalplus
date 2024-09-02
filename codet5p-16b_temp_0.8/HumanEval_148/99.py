
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

    import math
    if planet1 == "Mercury":
        planet1 = "Mercury Barycenter"
    if planet2 == "Mercury":
        planet2 = "Mercury Barycenter"

    if planet1 == "Venus":
        planet1 = "Venus Barycenter"
    if planet2 == "Venus":
        planet2 = "Venus Barycenter"

    if planet1 == "Earth":
        planet1 = "Earth Barycenter"
    if planet2 == "Earth":
        planet2 = "Earth Barycenter"

    if planet1 == "Mars":
        planet1 = "Mars Barycenter"
    if planet2 == "Mars":
        planet2 = "Mars Barycenter"

    if planet1 == "Jupiter":
        planet1 = "Jupiter Barycenter"
    if planet2 == "Jupiter":
        planet2 = "Jupiter Barycenter"

    if planet1 == "Saturn":
        planet1 = "Saturn Barycenter"
    if planet2 == "Saturn":
        planet2 = "Saturn B
