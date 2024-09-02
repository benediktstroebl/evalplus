
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
    #input
    planet1 = planet1.lower()
    planet2 = planet2.lower()
    #process
    #output
    if planet1 not in ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"] or planet2 not in ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]:
        return tuple()
    elif planet1 < planet2:
        return tuple(["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"][0:planet2.index(planet2) - planet1.index(planet1) + 1])
    elif planet1 > planet2:
        return tuple(["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"][planet1.index(planet1) - planet2.index
