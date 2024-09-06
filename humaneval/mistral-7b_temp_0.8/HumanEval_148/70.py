
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
    if planet1 == "Earth":
        planet1 = "earth"
    if planet2 == "Earth":
        planet2 = "earth"
    if planet1 == "Mercury":
        planet1 = "mercury"
    if planet2 == "Mercury":
        planet2 = "mercury"
    if planet1 == "Venus":
        planet1 = "venus"
    if planet2 == "Venus":
        planet2 = "venus"
    if planet1 == "Mars":
        planet1 = "mars"
    if planet2 == "Mars":
        planet2 = "mars"
    if planet1 == "Jupiter":
        planet1 = "jupiter"
    if planet2 == "Jupiter":
        planet2 = "jupiter"
    if planet1 == "Saturn":
        planet1 = "saturn"
    if planet2 == "Saturn":
        planet2 = "saturn"
    if planet1 == "Uranus":
        planet1 = "uranus"
    if planet
