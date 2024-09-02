
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
    if not (isinstance(planet1,str) and isinstance(planet2,str)):
        return ()
    if planet1 == "Mercury" or planet2 == "Mercury":
        return ("Mercury",)
    if planet1 == "Venus" or planet2 == "Venus":
        return ("Venus",)
    if planet1 == "Earth" or planet2 == "Earth":
        return ("Earth",)
    if planet1 == "Mars" or planet2 == "Mars":
        return ("Mars",)
    if planet1 == "Jupiter" or planet2 == "Jupiter":
        return ("Jupiter",)
    if planet1 == "Saturn" or planet2 == "Saturn":
        return ("Saturn",)
    if planet1 == "Uranus" or planet2 == "Uranus":
        return ("Uranus",)
    if planet1 == "Neptune" or planet2 == "Neptune":
        return ("Neptune",)
    if planet1 < planet2:
        start_index = 0
        for planet in planet1.split(","):
            if planet in planet2:
                return planet.split(","[start_index])
            start_index += 1
        return ()
    else:
        return planet2.split(",")[1:] + planet1.split(",")[:1]
