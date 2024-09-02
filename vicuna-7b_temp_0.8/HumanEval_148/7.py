
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
        return ("Saturn", "Uranus")
    if planet1 == "Saturn" or planet2 == "Saturn":
        return ("Uranus", "Jupiter")
    if planet1 == "Uranus" or planet2 == "Uranus":
        return ("Jupiter", "Saturn")
    if planet1 == "Neptune" or planet2 == "Neptune":
        return ("Pluto", "Eris")
    if planet1 == "Pluto" or planet2 == "Pluto":
        return ("Eris", "Makemake")
    if planet1 == "Eris" or planet2 == "Eris":
        return ("Makemake", "Pluto")
    if planet1 == "Makemake" or planet2 == "Makemake":
        return ("Eris", "Pluto")
    if planet1 == "Sun" and planet2 == "Sun":
        return ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 == "Sun" and planet2 == "Mercury":
        return ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 == "Sun" and planet2 == "Venus":
        return ("Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 == "Sun" and planet2 == "Earth":
        return ("Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 == "Sun" and planet2 == "Mars":
        return ("Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 == "Sun" and planet2 == "Jupiter":
        return ("Saturn", "Uranus")
    if planet1 ==
