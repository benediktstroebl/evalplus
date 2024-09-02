
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
    #TODO: Implement a function to check if the planets exist in the solar system
    if "Mercury" in str(planet1) and "Uranus" in str(planet2:
        if str(planet2) > str(planet1):
            return("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
        else:
            return("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    elif "Venus" in str(planet1) and "Neptune" in str(planet2:
        if str(planet2) > str(planet1):
            return("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
        else:
            return("Venus")
    elif "Earth" in str(planet1) and "Mars" in str(planet2:
        if str(planet2) > str(planet1):
            return("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
        else:
            return("Earth", "Mars")
    elif "Jupiter" in str(planet1) and "Saturn" in str(planet2:
        if str(planet2) > str(planet1):
            return("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
        else:
            return("Jupiter", "Saturn")
    elif "Uranus" in str(planet1) and "Neptune" in str(planet2:
        if str(planet2) > str(planet1):
            return("Mercury", "Venus", "Earth", "Mars",
