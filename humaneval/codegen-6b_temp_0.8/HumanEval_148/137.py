
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
    '''
    From wikipedia:
    Between two planets P and Q, the orbital distance is the distance between the 
    centers of the orbits. The orbital distance also includes the distance between 
    the two planets, and is measured in an orbital arc.

    Given the orbital distance between P and Q, the orbit of P and Q is a complete 
    orbit, meaning that P and Q orbit independently.

    The orbital radius of P is defined to be the distance between the centers of 
    the orbits around P and the center of the orbit of Q.
    '''
    Plist = ("Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    return tuple(x for x in Plist if planet1 in x) + tuple(x for x in Plist if planet2 in x)
