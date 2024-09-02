
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
    #start off with a list of all planets:
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    #check to see if planet1 and planet2 are in the list:
    if planet1 not in planets or planet2 not in planets:
        return ()
    #planets are ordered by distance from the sun, so if the two planets are 
    #in the right order, we can return planet2:
    if planets.index(planet1) < planets.index(planet2):
        return (planet2, )
    #if planet2 is before planet1, then we have to return planet1 up to planet2,
    #and then all the planets after planet2
    else:
        return tuple([x for x in planets if planets.index(x) < planets.index(planet2)] + [x for x in planets if planets.index(x) > planets.index(planet2)])
