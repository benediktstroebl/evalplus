
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
    # your code here
    if planet1.lower() == "mercury" or planet1.lower() == "venus" or planet1.lower() == "earth" or planet1.lower() == "mars" or planet1.lower() == "jupiter" or planet1.lower() == "saturn" or planet1.lower() == "uranus" or planet1.lower() == "neptune":
        if planet2.lower() == "mercury" or planet2.lower() == "venus" or planet2.lower() == "earth" or planet2.lower() == "mars" or planet2.lower() == "jupiter" or planet2.lower() == "saturn" or planet2.lower() == "uranus" or planet2.lower() == "neptune":
            orbit1 = find_orbit(planet1)
            orbit2 = find_orbit(planet2)
            if orbit1 != False and orbit2 != False:
                return tuple(sorted(list(set(orbit1).intersection(orbit2))))
            else:
                return ()
        else:
            return ()
    else:
        return ()
