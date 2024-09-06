
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
    # check if the input planets are correct
    if planet1.lower() != "mercury" and planet1.lower() != "venus" and planet1.lower() != "earth" and planet1.lower() != "mars" and 
       planet1.lower() != "jupiter" and planet1.lower() != "saturn" and planet1.lower() != "uranus" and planet1.lower() != "neptune":
        return tuple()
    
    if planet2.lower() != "mercury" and planet2.lower() != "venus" and planet2.lower() != "earth" and planet2.lower() != "mars" and 
       planet2.lower() != "jupiter" and planet2.lower() != "saturn" and planet2.lower() != "uranus" and planet2.lower() != "neptune":
        return tuple()
    
    # check the order of the planets
    if "mercury" <= planet1 <= "neptune" and "mercury" <= planet2 <= "neptune":
        return sorted((planet1, planet2), key=lambda x: (SOL_RADIUS[x], (x,)))
    else:
        return tuple()
