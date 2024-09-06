
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
    planets1 = ["Jupiter", "Earth", "Mars", "Venus", "Saturn", "Uranus", "Neptune"]
    planets2 = ["Mercury", "Venus", "Earth", "Mars", "Saturn", "Uranus", "Neptune"]
    planets1.sort()
    planets2.sort()
    if planet1 in planets1 and planet2 in planets2:
        planets = planets1.index(planet1) + 1, planets2.index(planet2) + 1
        return tuple(planets1[planets[0] : planets[1] + 1]), tuple(planets2[planets[1] : planets[2] + 1])
    else:
        
