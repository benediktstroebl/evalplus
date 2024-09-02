
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
    j = int(planet2[2])
    i = int(planet1[2])
    if planet1 == "Sun" or planet2 == "Sun":
        return ()
    if planet1 == "Earth" or planet2 == "Earth":
        return ("Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 == "Mars" and planet2 == "Earth":
        return ("Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 == "Mercury" and planet2 == "Venus":
        return ("Venus", "Uranus")
    if planet1 == "Venus" and planet2 == "Uranus":
        return ("Mercury", "Neptune")
    if planet1 == "Jupiter" and planet2 == "Mars":
        return ("Saturn", "Neptune")
    if planet1 == "Saturn" and planet2 == "Jupiter":
        return ("Earth", "Uranus")
    if planet1 == "Uranus" and planet2 == "Jupiter":
        return ("Earth", "Neptune")
    if planet1 == "Neptune" and planet2 == "Jupiter":
        return ("Earth", "Mars")
    if planet1 == "Jupiter" and planet2 == "Saturn":
        return ("Mercury", "Mars")
    if planet1 == "Saturn" and planet2 == "Saturn":
        return ("Uranus")
    if planet1 == "Uranus" and planet2 == "Saturn":
        return ("Neptune")
    if planet1 == "Neptune" and planet2 == "Saturn":
        return ("Pluto")
    if planet1 == "Mercury" and planet2 == "Neptune":
        return ("Venus", "Mars")
    if planet1 == "Venus" and planet2 == "Neptune":
        return ("Mercury", "Jupiter")
    if planet1 == "Venus" and planet2 == "Jupiter":
        return ("Mars", "Saturn")
    if planet1 == "Venus" and planet2 == "Mars":
        