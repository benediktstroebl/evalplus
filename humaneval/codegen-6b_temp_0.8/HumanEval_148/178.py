
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
    planetDict = {
    "Mercury": [0, "Mercury", -1], 
    "Venus": [0, "Venus", -4], 
    "Earth": [0, "Earth", -3], 
    "Mars": [0, "Mars", -5], 
    "Jupiter": [0, "Jupiter", -6], 
    "Saturn": [0, "Saturn", -9], 
    "Uranus": [0, "Uranus", -8], 
    "Neptune": [0, "Neptune", -10], 
    }
    planets = []
    for planet in planetDict.keys():
        if planet1 == planet:
            planets.append(planet)

    for planet in planets:
        planetDict[planet][0] += 1

    for planet in planetDict.keys():
        if planetDict[planet][0] > planetDict[planet1][0] :
            planets.append(planet)
    
    planets.sort()

    return tuple(planets)
