
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

    planet_names = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    for planet in planet_names:
        if planet1 == planet or planet2 == planet:
            planet1 = planet
            planet2 = planet
    if planet1 == "Mercury" and planet2 == "Venus":
        return ("Venus")
    elif planet1 == "Mercury" and planet2 == "Earth":
        return ("Venus", "Earth")
    elif planet1 == "Mercury" and planet2 == "Mars":
        return ("Venus", "Earth", "Mars")
    elif planet1 == "Mercury" and planet2 == "Jupiter":
        return ("Venus", "Earth", "Mars", "Jupiter")
    elif planet1 == "Mercury" and planet2 == "Saturn":
        return ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    elif planet1 == "Mercury" and planet2 == "Uranus":
        return ("Ven
