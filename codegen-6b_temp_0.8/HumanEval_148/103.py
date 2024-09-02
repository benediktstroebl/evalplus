
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
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    output = []
    for planet in planets:
        if planet == planet1 or planet == planet2:
            continue
        elif planet1 == "Mercury" and planet2 == "Venus" and planet == "Mars":
            continue
        elif planet1 == "Venus" and planet2 == "Earth" and planet == "Mars":
            continue
        elif planet1 == "Earth" and planet2 == "Mars" and planet == "Jupiter":
            continue
        elif planet1 == "Mars" and planet2 == "Jupiter" and planet == "Saturn":
            continue
        elif planet1 == "Jupiter" and planet2 == "Saturn" and planet == "Uranus":
            continue
        elif planet1 == "Saturn" and planet2 == "Uranus" and planet == "Neptune":
            continue
        elif planet1 == "Uranus" and planet2 == "Neptune" and planet == "Venus":
            continue
        elif planet1 == "Neptune" and planet2 == "Venus" and planet == "Earth":
            continue
        elif planet1 == "Venus" and planet2 == "Earth" and planet == "Jupiter":
            continue
        elif planet1 == "Earth" and planet2 == "Jupiter" and planet == "Mars":
            continue
        elif planet1 == planet2:
            continue
        if planet1 == planet2:
            continue
        if planet1 == planet2:
            continue
        else:
            output += (planet,)

    return tuple(sorted(output))
