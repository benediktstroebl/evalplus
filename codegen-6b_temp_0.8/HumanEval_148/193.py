
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
    planets = {"Mercury":"0:0", "Venus":"0:60", "Earth":"1:0", "Mars":"1:60", "Jupiter":"2:0", 
                "Saturn":"2:60", "Uranus":"3:0", "Neptune":"3:60"}
    
    planets1 = planets[planet1]
    planets2 = planets[planet2]
    planetList = []
    
    for i,j in planets.items():
        if planets1 < j and planets2 > j:
            planetList.append(i)
    
    return tuple(sorted(planetList))
