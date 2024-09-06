
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

    orbits = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in orbits or planet2 not in orbits:
        return ()
    elif planet1 == "Earth" and planet2 == "Mercury":
        return orbits[:2]
    elif planet1 == "Earth" and planet2 == "Mars":
        return orbits[:3]
    elif planet1 == "Earth" and planet2 == "Jupiter":
        return orbits[:4]
    elif planet1 == "Earth" and planet2 == "Saturn":
        return orbits[:5]
    elif planet1 == "Earth" and planet2 == "Uranus":
        return orbits[:6]
    elif planet1 == "Earth" and planet2 == "Neptune":
        return orbits[:7]
    elif planet1 == "Mercury" and planet2 == "Mars":
        return orbits[1:3]
    elif planet1 == "
