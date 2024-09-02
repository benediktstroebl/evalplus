
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

    if planet1 == "Mercury":
        planet1_orbital = 0
    elif planet1 == "Venus":
        planet1_orbital = 1
    elif planet1 == "Earth":
        planet1_orbital = 2
    elif planet1 == "Mars":
        planet1_orbital = 3
    elif planet1 == "Jupiter":
        planet1_orbital = 4
    elif planet1 == "Saturn":
        planet1_orbital = 5
    elif planet1 == "Uranus":
        planet1_orbital = 6
    elif planet1 == "Neptune":
        planet1_orbital = 7
    
    if planet2 == "Mercury":
        planet2_orbital = 0
    elif planet2 == "Venus":
        planet2_orbital = 1
    elif planet2 == "Earth":
        planet2_orbital = 2
    elif planet2 == "Mars":
        planet2_orbital = 3
    elif planet2 == "Jupiter":
        planet2_orbital =
