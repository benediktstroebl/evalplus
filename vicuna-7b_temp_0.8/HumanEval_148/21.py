
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
    if planet1 == "Jupiter" or planet2 == "Jupiter":
        jup = ["Jupiter"]
    elif planet1 == "Saturn" or planet2 == "Saturn":
        saturn = ["Saturn"]
    elif planet1 == "Uranus" or planet2 == "Uranus":
        uranus = ["Uranus"]
    elif planet1 == "Neptune" or planet2 == "Neptune":
        neptune = ["Neptune"]
    elif planet1 == "Venus" or planet2 == "Venus":
        venus = ["Venus"]
    elif planet1 == "Mars" or planet2 == "Mars":
        mars = ["Mars"]
    elif planet1 == "Earth" or planet2 == "Earth":
        earth = ["Earth"]
    else:
        return []

    midpoint = [float("inf"), float("-inf")]
    for planet in jup + saturn + uranus + neptune + venus + mars + earth:
        distance = distance(planet1, planet)
        if distance < midpoint[0]:
            midpoint[0] = distance
        elif distance > midpoint[1]:
            midpoint[1] = distance

    return [earth[0], mars[0], jupiter[0], venus[0], uranus[0], neptune[0], planet1, planet2]
