
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
        return("Venus")
    elif planet1 == "Venus":
        return("Earth", "Mars", "Jupiter", "Saturn")
    elif planet1 == "Earth":
        return("Mars", "Jupiter", "Saturn")
    elif planet1 == "Mars":
        return("Jupiter", "Saturn")
    elif planet1 == "Jupiter":
        return("Saturn")
    elif planet1 == "Saturn":
        return("Uranus")
    elif planet1 == "Uranus":
        return("Neptune")
    elif planet1 == "Neptune":
        return()
    elif planet1 not in ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"):
        return()

    # Repeat the same but for planet2
    if planet2 == "Mercury":
        return("Venus")
    elif planet2 == "Venus":
        return("Earth", "Mars", "Jupiter", "Saturn")
    elif planet2 == "Earth":
        return("Mars", "Jupiter", "Saturn")
    elif planet2 == "Mars":
        return("Jupiter", "Saturn")
    elif planet2 == "Jupiter":
        return("Saturn")
    elif planet2 == "Saturn":
        return("Uranus")
    elif planet2 == "Uranus":
        return("Neptune")
    elif planet2 == "Neptune":
        return()
    elif planet2 not in ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"):
        return()

    # Now let's make a list of planets between planet1 and planet2
    planets_between = list()
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jup
