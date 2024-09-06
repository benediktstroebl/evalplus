
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
    # Please print a list of string
    if planet1 == "Mercury":
        return ["Venus"]
    elif planet1 == "Earth":
        return ["Venus", "Mars", "Jupiter", "Saturn"]
    elif planet1 == "Venus":
        return ["Earth", "Mars", "Jupiter", "Saturn"]
    elif planet1 == "Mars":
        return ["Earth", "Jupiter", "Saturn"]
    elif planet1 == "Jupiter":
        return ["Earth", "Saturn"]
    elif planet1 == "Saturn":
        return ["Earth"]
    elif planet1 == "Uranus":
        return ["Earth", "Mars", "Jupiter", "Saturn"]
    elif planet1 == "Neptune":
        return ["Earth", "Mars", "Jupiter", "Saturn"]
    else:
        return []
